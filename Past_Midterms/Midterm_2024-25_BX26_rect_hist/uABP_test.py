# -*- coding: utf-8 -*-
# this file is designed to import rect_hist.py
if __name__ != '__main__':
    assert False, "You must NOT import this file from uABP.py"

import uABP as sol
import uABP_test_extra as tst
import timeit
import random

grading_mode = False # set to True to make unimplemented function error out


def test_MV_vectors():
    if sol.MV_vectors([[[[1, 1]]]]) is None:
        print('skipping MV_vectors (unimplemented)')
        assert not grading_mode
        return
    print('testing MV_vectors...')
    for (n,d) in tst.M:
        assert tst.Vct[n,d] == sol.MV_vectors(tst.M[n,d]), "\n\nThere is a problem with the following uABP of size " + str([n,d]) + " given by \n\n M = " + str(tst.M[n,d]) + " \n\nThe correct answer should be \n\n " + str(tst.Vct[n,d]) + "\n"
    print('test MV_vectors() passed')
    print('\n================================== \n')

def test_MM_matrix():
    if sol.MM_matrix([[[[1, 1]]]]) is None:
        print('skipping MM_matrix (unimplemented)')
        assert not grading_mode
        return
    print('testing MV_matrix...')
    for (n,d) in tst.M:
        assert tst.Mat[n,d] == sol.MM_matrix(tst.M[n,d]), "\n\nThere is a problem with the following uABP of size " + str([n,d]) + " given by \n\n M = " + str(tst.M[n,d]) + " \n\nThe correct answer should be \n\n" + str(tst.Mat[n,d]) + "\n"
    print('test MM_matrix() passed')
    print('\n================================== \n')

def test_eval_MV_PIT():
    if sol.eval_MV_PIT([[[[1, 1]]]], 1) is None:
        print('skipping eval_MV_PIT (unimplemented)')
        assert not grading_mode
        return
    print('testing eval_MV_PIT() ...')
    for (n,d) in tst.M:
        for pp in tst.Evp[n,d]:
            assert pp[1] == sol.eval_MV_PIT(tst.M[n,d], pp[0]), "\n\nThere is a problem with the following uABP of size " + str([n,d]) + " given by \n\nM = " + str(tst.M[n,d]) + " \n\n at the point p = " + str(pp[0]) + "\n\nThe correct answer should be \n\n" + str(pp[1]) + "\n"
    print('test eval_MV_PIT() passed')
    print('\n================================== \n')


def create_conseq_sols_uABP(n,d):
    return [[[[ -k , 1] for j in range(n)] for i in range(n)] for k in range(d)]

    
def test_MC_eval_PIT():
    if sol.MC_eval_PIT([[[[1, 1]]]],range(10)) is None:
        print('skipping MC_eval_PIT (unimplemented)')
        assert not grading_mode
        return
    print('testing MC_eval_PIT() ...')
    Meq1 = [ [ [[1,1],[0,1]], [[2,3], [1,4]] ], [ [[1,2],[1,2]], [[3,5], [7,3]] ], [ [[1,6],[2,5]], [[2,5], [3,1]] ] ]
    Meq2 = [ [ [[1,1],[1,3]], [[2,3], [1,-1]] ], [ [[1,2],[1,3]], [[1,1], [1,4]] ], [ [[1,3],[2,5]], [[-1,-1], [3,1]] ] ]
    Mconsq = create_conseq_sols_uABP(1,20)
    assert sum([sol.MC_eval_PIT(Meq1,range(4)) for i in range(100)]) == 0, "\n\nYour algorithm says that the example corresponding to Eq. 1 in the PDF is equal to zero, but we are considering a set S = {0,1,2,3} that contains no solution of the polynomial\n Example: \n" + str(Meq1)
    assert sum([sol.MC_eval_PIT(Meq2,range(10)) for i in range(100)]) == 100, "\\nnYour algorithm says that the example corresponding to Eq. 2 in the PDF is equal not equal to zero, but it is. \n Example: \n" + str(Meq2)
    fiftyP = sum([sol.MC_eval_PIT(Mconsq,range(21)) for i in range(2000)])
    assert fiftyP < 1090, "\n\nIn the example given by the polynomial that vanishes at {0,...,19} that is,\n" + str(Mconsq) + "\n, and S = {0,...,20}, your algorithm says that this polynomial is zero with a much higher probability than 1/2. You are not trying enough points."
    assert 910 < fiftyP, "\n\nIn the example given by the polynomial that vanishes at {0,...,19} that is,\n" + str(Mconsq) + "\n, and S = {0,...,20}, your algorithm says that this polynomial is zero with a much lower probability than 1/2. You might be trying too many points or your experiments are not independent!"
    print('test eval_MV_PIT() passed!')
    print('\n================================== \n')
    
test_MV_vectors()

test_MM_matrix()

test_eval_MV_PIT()

test_MC_eval_PIT()

print("Don\' forget to add the explanations!")
