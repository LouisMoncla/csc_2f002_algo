# CSC_2F002_EP: Design and Analysis of Algorithms (S3)

Lectures, tutorials (TD), exercises and past exams for the École Polytechnique algorithms course. Code is in Python.
Topics: divide and conquer, randomization, amortization, string algorithms, P vs NP.

## Layout

| Folder | Content |
|---|---|
| `TD1` ... `TD8` | tutorial statement (`TDnn.pdf`) + my solutions and tests |
| `Lectures` | slides (`LectureNN_Topic`), blackboard proofs (`LectureNN_BlackBoardProofs`), merged lectures |
| `Complexity_exercises` | weekly exercises (`WeekNN_Exos`) and solutions (`..._Sol`) |
| `Past_Midterms` | one folder per exam, `Midterm_<year>_<promotion>_<file>`: PDF + code |
| `Past_Finals` | `Final_<year>_<promotion>` |
| `Correction_TD_BX26` | past TD corrections (BX26) |

## Tutorials

| TD | Topic | Code |
|---|---|---|
| 1 | Powering and addition chains | `chains.py`, `PowerTree.py` |
| 2 | Fast multiplication (polynomials, matrices) | `mult.py`, `strassen.py` |
| 3 | Divide and conquer on arrays | `search.py` |
| 4 | Peaks in arrays and 2D grids | `peaks.py` |
| 5 | Divide and conquer + randomization | `L_tiling.py`, `MultiGraph.py` |
| 6 | Fingerprinting for text search | `search.py` |
| 7 | SAT solving for Latin squares (Sudokus) | `Sat.py`, `LatinSquarePuzzle.py` |
| 8 | Union-Find case studies | `uf.py`, `Hex.py`, `perco.py`, `erdos.py` |

Run a TD's tests from its folder, e.g. `cd TD4 && python test_peaks.py`.

## Naming

`S3_Algo_<Type><NN>`; `_Sol` = with solutions; `BXnn` = promotion that sat the exam (e.g. BX25).
