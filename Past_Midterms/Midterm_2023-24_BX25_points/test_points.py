# -*- coding: utf-8 -*-

from points import *

def test_min_max():
    A1 = [3,12,10,2,0,4]
    A2 = [2,1,10,2,12,4,3]
    if min_max(A1) is None:
        print("***** skipping min_max (unimplemeneted)")
        return
    r1,r2 = min_max(A1)
    if (not ((r1 == 0 and r2 == 12) or (r1 == 12 and r2 == 0))):
        print("***** min_max\n your result\n {}\n is wrong for the array\n {}\n*****".format([r1,r2],A1))
    r1,r2 = min_max(A2)
    if (not ((r1 == 1 and r2 == 12) or (r1 == 12 and r2 == 1))):
        print("***** min_max\n your result\n {}\n is wrong for the array\n {}\n*****".format([r1,r2],A2))

def test_bounding_box():
    S1 = [[2,6],[3,7],[4,6],[6,4],[8,5]]
    S2 = [[2,6],[3,7],[4,5],[6,4],[8,6],[9,3],[10,2],[11,2]]
    if bounding_box(S1) is None:
        print("***** skipping bounding_box (unimplemeneted)")
        return
    R = bounding_box(S1)
    if (not (((R[0][0] == 2 and R[0][1] == 7) and (R[1][0] == 8 and R[1][1] == 4)) or ((R[0][0] == 8 and R[0][1] == 4) and (R[1][0] == 2 and R[1][1] == 7)))):
        print("***** bounding_box\n your result\n {}\n is wrong for the set\n {}\n*****".format(R,S1))
    R = bounding_box(S2)
    if (not (((R[0][0] == 2 and R[0][1] == 7) and (R[1][0] == 11 and R[1][1] == 2)) or ((R[0][0] == 11 and R[0][1] == 2) and (R[1][0] == 2 and R[1][1] == 7)))):
        print("***** bounding_box\n your result\n {}\n is wrong for the set\n {}\n*****".format(R,S2))
        
def test_maxima_set():
    S1 = [[2,6],[3,7],[4,6],[6,4],[8,5]]
    S2 = [[2,6],[3,7],[4,5],[6,4],[8,6],[9,3],[10,2],[11,2]]
    if maxima_set(S1) is None:
        print("***** skipping maxima_set (unimplemeneted)")
        return
    R = maxima_set(S1)
    if ([3,7] not in R) or ([4,6] not in R) or ([8,5] not in R):
        print("***** maxima_set\n your result\n {}\n is wrong for the set\n {}\n*****".format(R,S1))
    R = maxima_set(S2)
    if ([3,7] not in R) or ([9,3] not in R) or ([8,6] not in R) or ([9,3] not in R) or ([11,2] not in R):
        print("***** maxima_set\n your result\n {}\n is wrong for the set\n {}\n*****".format(R,S2))
        


def min_distance_trivial(S):
    delta = 4
    k1 = [0,0]
    k2 = [0,0]
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            deltap = math.dist(S[i], S[j])
            if deltap < delta:
                delta = deltap
                k1 = S[i]
                k2 = S[j]
    return delta, k1, k2



def test_min_distance():
    S1 = [[.2,.3],[.1,.5],[.0,.4],[.4,.7],[.2,.9],[.1,.5]]
    if min_distance(S1) is None:
        print("***** skipping min_distance (unimplemeneted)")
        return
    spec = min_distance_trivial(S1)
    yours = min_distance(S1)
    if (spec[0] != yours[0]):
        print("***** maxima_set\n your result\n {}\n is wrong for the set\n {}.\n It should be {}\n*****".format(yours[0],S1,spec[0]))
    else:
        print("The result of brute force: ", min_distance_trivial(S1))
        print("Your result: ", min_distance(S1))
        print("Your implementation may be correct even if the points above differ (if there are multiple pairs of points at the same distance, then the results may differ)")

test_min_max()
test_bounding_box()
test_maxima_set()
test_min_distance()
