# -*- coding: utf-8 -*-
# Tests for the mock midterm, Problem 1 (sorting networks).
#   python3 test_networks.py        -> test every question, in order
#   python3 test_networks.py 4      -> test Q4 only
#   python3 test_networks.py 1 2    -> test Q1 and Q2
#   (works the same with `%run test_networks.py 4` in IPython)
#
# A function is skipped (unimplemented) while its body is still `raise NotImplementedError` (or
# `pass`, `return None`). As soon as you write something, it is checked on the figures of the
# statement, small hand-made cases, and many random inputs of increasing size (compared with an
# obviously-correct reference). Only correctness is tested, not running time.
# On failure you get the smallest input that breaks your code. If your code raises an error, the
# error and the line of networks.py are shown, and the next functions are still tested.

import sys
import ast
import copy
import inspect
import itertools
import textwrap
import traceback
import signal
import random
import importlib

import networks
networks = importlib.reload(networks)   # IPython's %run would otherwise keep an old version

TIME_LIMIT = 2.0   # seconds per call; more than that is treated as an infinite loop


# ---------------------------------------------------------------- data of the statement

NET4 = [(0, 1), (2, 3), (0, 2), (1, 3), (1, 2)]                         # Figure 1
FIG1_IN = [3, 1, 4, 2]
FIG1_STEPS = [[3, 1, 4, 2], [1, 3, 4, 2], [1, 3, 2, 4], [1, 3, 2, 4], [1, 3, 2, 4], [1, 2, 3, 4]]
FIG2_IN = [0, 1, 1, 1, 1, 1, 0, 0]                                      # Figure 2
FIG2_OUT = [0, 1, 0, 0, 1, 1, 1, 1]


# ---------------------------------------------------------------- references (slow but obviously correct)

def ref_apply(net, A):
    B = list(A)
    for i, j in net:
        if B[i] > B[j]:
            B[i], B[j] = B[j], B[i]
    return B

def all01(n):
    return [list(t) for t in itertools.product((0, 1), repeat=n)]

def ref_sorts(net, n):
    return all(ref_apply(net, A) == sorted(A) for A in all01(n))

def ref_bitonic01_lists(n):
    """All bitonic 0/1 lists of length n: the forms 0^a 1^b 0^c and 1^a 0^b 1^c."""
    out = set()
    for a in range(n + 1):
        for b in range(n + 1 - a):
            c = n - a - b
            out.add((0,) * a + (1,) * b + (0,) * c)
            out.add((1,) * a + (0,) * b + (1,) * c)
    return [list(t) for t in sorted(out)]

def ref_is_bitonic01(A):
    return tuple(A) in {tuple(B) for B in ref_bitonic01_lists(len(A))}

def ref_bubble(n):
    """The statement's order: for i = n-1, ..., 1, the comparators (0,1), (1,2), ..., (i-1,i)."""
    return [(t, t + 1) for i in range(n - 1, 0, -1) for t in range(i)]

def ref_half_cleaner(lo, n, up):
    h = n // 2
    return [(lo + t, lo + t + h) if up else (lo + t + h, lo + t) for t in range(h)]

def ref_depth(net):
    """Copy of the given depth(net) (greedy layering)."""
    layer = {}
    d = 0
    for i, j in net:
        t = 1 + max(layer.get(i, 0), layer.get(j, 0))
        layer[i] = layer[j] = t
        d = max(d, t)
    return d

def rand_net(rng, n, size):
    """A random network on n wires, comparators in both directions."""
    return [tuple(rng.sample(range(n), 2)) for _ in range(size)]

def rand_bitonic(rng, n, vmax=50):
    """A random bitonic list of integers: increasing then decreasing, then a cyclic shift."""
    p = rng.randrange(n + 1)
    vals = [rng.randrange(vmax) for _ in range(n)]
    A = sorted(vals[:p]) + sorted(vals[p:], reverse=True)
    s = rng.randrange(n)
    return A[s:] + A[:s]

def log2(n):
    return n.bit_length() - 1


# ---------------------------------------------------------------- harness

class Fail(Exception):
    """A failed check; its message is the sentence printed after `Testing ...`."""

class _Timeout(Exception):
    pass

def _on_alarm(signum, frame):
    raise _Timeout()

signal.signal(signal.SIGALRM, _on_alarm)

def _is_stub(f):
    """True while the body of f is only a docstring and `raise NotImplementedError` / `pass` / `return None`."""
    try:
        tree = ast.parse(textwrap.dedent(inspect.getsource(f)))
    except (OSError, TypeError):
        return False
    body = tree.body[0].body
    if body and isinstance(body[0], ast.Expr) and isinstance(getattr(body[0], "value", None), ast.Constant) \
            and isinstance(body[0].value.value, str):
        body = body[1:]
    if len(body) != 1:
        return False
    stmt = body[0]
    if isinstance(stmt, ast.Pass):
        return True
    if isinstance(stmt, ast.Return) and (stmt.value is None or
                                         (isinstance(stmt.value, ast.Constant) and stmt.value.value is None)):
        return True
    if isinstance(stmt, ast.Expr) and isinstance(stmt.value, ast.Constant) and stmt.value.value is Ellipsis:
        return True
    if isinstance(stmt, ast.Raise) and stmt.exc is not None:
        exc = stmt.exc.func if isinstance(stmt.exc, ast.Call) else stmt.exc
        return isinstance(exc, ast.Name) and exc.id == "NotImplementedError"
    return False

def _fmt(args):
    return "(" + ", ".join(_short(a) for a in args) + ")"

def _short(x):
    if isinstance(x, list) and len(x) > 12:
        head = ", ".join(repr(e) for e in x[:4])
        return f"[{head}, ..., {x[-1]!r}]  ({len(x)} elements)"
    s = repr(x)
    return s if len(s) <= 110 else s[:107] + "..."

def _where(exc):
    """` (line N of networks.py)` for the deepest frame of networks.py in the traceback of exc."""
    line = None
    for fr in traceback.extract_tb(exc.__traceback__):
        if fr.filename.endswith("networks.py") and not fr.filename.endswith("test_networks.py"):
            line = fr.lineno
    return f" (line {line} of networks.py)" if line else ""

def call(f, *args, limit=None):
    """Run f(*args) with a time limit; check the inputs are not modified. Return (result, shown call)."""
    limit = limit or TIME_LIMIT
    before = copy.deepcopy(args)
    shown = f"{f.__name__}{_fmt(before)}"
    signal.setitimer(signal.ITIMER_REAL, limit)
    try:
        got = f(*args)
    except _Timeout:
        raise Fail(f"your {shown} did not finish in {limit}s (infinite loop?)")
    except Exception as e:
        signal.setitimer(signal.ITIMER_REAL, 0)
        msg = str(e).splitlines()[0] if str(e) else ""
        raise Fail(f"your {shown} crashed: {type(e).__name__}: {msg}{_where(e)}")
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
    if list(args) != list(before):
        raise Fail(f"your {f.__name__} modified a list passed as a parameter, do not do that!")
    return got, shown

def wrong(shown, got, want):
    returned = "None (nothing returned)" if got is None else _short(got)
    raise Fail(f"your {shown} returned {returned} instead of {_short(want)}")

def as_network(shown, net, lo, n):
    """Check that net is a list of comparators (i, j) of distinct wires in lo..lo+n-1; return it as tuples."""
    if not isinstance(net, list):
        raise Fail(f"your {shown} returned {_short(net)}, it should return a list of comparators (i, j)")
    out = []
    for c in net:
        try:
            i, j = c
        except (TypeError, ValueError):
            raise Fail(f"your {shown} returned the comparator {c!r}, a comparator is a pair (i, j)")
        if not (isinstance(i, int) and isinstance(j, int)):
            raise Fail(f"your {shown} returned the comparator {c!r}, wires must be integers")
        if i == j:
            raise Fail(f"your {shown} returned the comparator {c!r}, its two wires must be different")
        if not (lo <= i < lo + n and lo <= j < lo + n):
            raise Fail(f"your {shown} returned the comparator {c!r}, outside the wires {lo}..{lo + n - 1}")
        out.append((i, j))
    return out


# ---------------------------------------------------------------- checks of one call

def check_apply(net, A):
    got, shown = call(networks.apply_network, net, A)
    if got is A:
        raise Fail(f"your {shown} returned the input list itself, it must return a new list")
    want = ref_apply(net, A)
    if got != want:
        wrong(shown, got, want)

def check_is_bitonic01(A):
    got, shown = call(networks.is_bitonic01, A)
    want = ref_is_bitonic01(A)
    if got is not want:
        wrong(shown, got, want)

def check_is_sorting(net, n):
    got, shown = call(networks.is_sorting_network, net, n)
    want = ref_sorts(net, n)
    if got is not want:
        wrong(shown, got, want)

def check_bubble(n):
    got, shown = call(networks.bubble_network, n)
    net = as_network(shown, got, 0, n)
    want = ref_bubble(n)
    if net != want:
        wrong(shown, got, want)

def check_half_cleaner(lo, n, up):
    got, shown = call(networks.half_cleaner, lo, n, up)
    net = as_network(shown, got, lo, n)
    want = ref_half_cleaner(lo, n, up)
    if sorted(net) != sorted(want):
        wrong(shown, got, want)

def check_merger(lo, n, up, rng):
    got, shown = call(networks.bitonic_merger, lo, n, up)
    net = as_network(shown, got, lo, n)
    for A in ref_bitonic01_lists(n) + [rand_bitonic(rng, n) for _ in range(20)]:
        out = ref_apply(net, [-1] * lo + A)[lo:]
        want = sorted(A, reverse=not up)
        if out != want:
            raise Fail(f"your {shown} does not sort the bitonic input {_short(A)}: "
                       f"its output is {_short(out)} instead of {_short(want)}")
    k = log2(n)
    if len(net) != (n // 2) * k:
        raise Fail(f"your {shown} has {len(net)} comparators, the construction of the statement "
                   f"(half-cleaner + two mergers) gives (n/2)*log2(n) = {(n // 2) * k}")

def check_sorter(n, rng):
    got, shown = call(networks.bitonic_sorter, n)
    net = as_network(shown, got, 0, n)
    inputs = all01(n) if n <= 8 else []
    inputs += [[rng.randrange(-100, 100) for _ in range(n)] for _ in range(20)]
    inputs += [[rng.randrange(3) for _ in range(n)] for _ in range(5)]
    for A in inputs:
        out = ref_apply(net, A)
        if out != sorted(A):
            raise Fail(f"your {shown} does not sort {_short(A)}: its output is {_short(out)}")
    k = log2(n)
    size, d = n * k * (k + 1) // 4, k * (k + 1) // 2
    if len(net) != size:
        raise Fail(f"your {shown} has {len(net)} comparators, the bitonic sorter of the statement "
                   f"has n*k(k+1)/4 = {size} (k = log2(n))")
    if ref_depth(net) != d:
        raise Fail(f"your {shown} has depth {ref_depth(net)}, the bitonic sorter of the statement "
                   f"has depth k(k+1)/2 = {d} (k = log2(n))")


# ---------------------------------------------------------------- tests

def test_apply_network():
    # Figure 1, comparator after comparator
    for s in range(len(NET4) + 1):
        check_apply(NET4[:s], FIG1_IN)
        if ref_apply(NET4[:s], FIG1_IN) != FIG1_STEPS[s]:      # sanity check of the test itself
            raise AssertionError("bad data in test_networks.py")
    for net, A in [([], [5, 3]), ([(0, 1)], [2, 1]), ([(0, 1)], [1, 2]), ([(1, 0)], [1, 2]),
                   ([(1, 0)], [2, 1]), ([(0, 2)], [7, 0, 7]), ([(2, 0)], [1, 5, 3]),
                   ([(0, 1), (1, 0)], [4, 9]), ([(3, 0), (2, 1)], [1, 2, 3, 4]), ([], [8])]:
        check_apply(net, A)
    rng = random.Random(1)
    for n in range(2, 13):
        for _ in range(15):
            net = rand_net(rng, n, rng.randrange(0, 3 * n))
            check_apply(net, [rng.randrange(-20, 20) for _ in range(n)])
        check_apply(rand_net(rng, n, 2 * n), [rng.randrange(3) for _ in range(n)])   # repeated values
        check_apply(ref_bubble(n), [rng.randrange(100) for _ in range(n)])

def test_is_bitonic01():
    for A in [[0, 1, 1, 0], [1, 0, 0, 1], [0, 1, 0, 1], [], [1], [0, 0], [0, 0, 1], [1, 1, 0, 0, 0, 1],
              [1, 0, 1, 0], [0, 1, 1, 0, 1]]:
        check_is_bitonic01(A)
    for n in range(0, 11):
        for A in all01(n):
            check_is_bitonic01(A)

def test_is_sorting_network():
    check_is_sorting(NET4, 4)
    for t in range(len(NET4)):                              # remove one comparator: no longer sorts
        check_is_sorting(NET4[:t] + NET4[t + 1:], 4)
    for net, n in [([], 1), ([(0, 1)], 2), ([(1, 0)], 2), ([], 2), ([(0, 1), (1, 2)], 3),
                   ([(0, 1), (1, 2), (0, 1)], 3), ([(1, 2), (0, 1), (1, 2)], 3),
                   ([(0, 1), (2, 3), (0, 2), (1, 3)], 4), ([(1, 0), (3, 2), (2, 0), (3, 1), (2, 1)], 4)]:
        check_is_sorting(net, n)
    for n in range(2, 8):
        check_is_sorting(ref_bubble(n), n)
        check_is_sorting(ref_bubble(n)[:-1], n)
    rng = random.Random(2)
    for n in range(2, 7):
        for _ in range(40):
            check_is_sorting(rand_net(rng, n, rng.randrange(0, 3 * n)), n)
        for _ in range(10):                                 # sorting networks, then one comparator reversed
            net = ref_bubble(n)
            t = rng.randrange(len(net))
            net[t] = net[t][::-1]
            check_is_sorting(net, n)

def test_bubble_network():
    for n in range(1, 13):
        check_bubble(n)

def test_half_cleaner():
    for lo, n, up in [(0, 2, True), (0, 2, False), (0, 4, True), (4, 4, False), (0, 8, True),
                      (3, 8, False), (5, 16, True), (2, 16, False), (0, 32, True), (7, 32, False)]:
        check_half_cleaner(lo, n, up)
    got, shown = call(networks.half_cleaner, 0, 8, True)                # Figure 2
    out = ref_apply(as_network(shown, got, 0, 8), FIG2_IN)
    if out != FIG2_OUT:
        raise Fail(f"on the input {FIG2_IN} of Figure 2, your {shown} gives {out} instead of {FIG2_OUT}")

def test_bitonic_merger():
    rng = random.Random(4)
    for k in range(0, 6):
        for lo in (0, 3, 5):
            for up in (True, False):
                check_merger(lo, 2 ** k, up, rng)

def test_bitonic_sorter():
    got, shown = call(networks.bitonic_sorter, 1)
    if got != []:
        wrong(shown, got, [])
    got, shown = call(networks.bitonic_sorter, 2)
    if as_network(shown, got, 0, 2) != [(0, 1)]:
        wrong(shown, got, [(0, 1)])
    rng = random.Random(5)
    for k in range(1, 9):
        check_sorter(2 ** k, rng)

MODULE = networks

QUESTIONS = [
    # (question, function, test)
    (1, "apply_network",      test_apply_network),
    (2, "is_bitonic01",       test_is_bitonic01),
    (2, "is_sorting_network", test_is_sorting_network),
    (3, "bubble_network",     test_bubble_network),
    (4, "half_cleaner",       test_half_cleaner),
    (4, "bitonic_merger",     test_bitonic_merger),
    (5, "bitonic_sorter",     test_bitonic_sorter),
]


# ---------------------------------------------------------------- running

def run(num, name, test):
    """Print `Testing name...` then [ok] or what went wrong. Return "ok", "fail" or "skip"."""
    f = getattr(MODULE, name, None)
    if f is None:
        print(f"skipping {name} (not found in {MODULE.__name__}.py)")
        return "skip"
    if _is_stub(f):
        print(f"skipping {name} (unimplemented)")
        return "skip"
    print(f"Testing {name}...".ljust(WIDTH), end="", flush=True)
    try:
        test()
    except Fail as e:
        print(e)
        return "fail"
    print("[ok]")
    return "ok"

WIDTH = 4 + max(len(f"Testing {name}...") for _, name, _ in QUESTIONS)

wanted = {int(a.lstrip("qQ")) for a in sys.argv[1:]}
results = {name: run(num, name, test) for num, name, test in QUESTIONS if not wanted or num in wanted}
print()
for kind, label in [("ok", "correct"), ("fail", "wrong"), ("skip", "not done")]:
    names = [n for n, r in results.items() if r == kind]
    if names:
        print(f"{label + ':':10}{', '.join(names)}")
