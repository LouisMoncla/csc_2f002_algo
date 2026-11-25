# -*- coding: utf-8 -*-
"""
Given a uABP, check if it is zero or not.
"""
import math
import random

def poly_mult(P,Q):
    n=len(P)
    m=len(Q)
    R=[0 for i in range(m+n-1)]
    for i in range(n):
        for j in range(m):
            R[i+j]=R[i+j]+P[i]*Q[j]
    return R   

def poly_add(P,Q): 
   n=len(P)
   m=len(Q)
   R=[0 for i in range(max(m,n))]
   for i in range(n):
       R[i]+=P[i]
   for i in range(m):
       R[i]+=Q[i]
   return R    
         
def neg(P):
   return [-P[i] for i in range(len(P))]
   
def shift(P,k):
   return [0 for i in range(k)]+[P[i] for i in range(len(P))]

def poly_kara_mult(P,Q):
    #assert len(P) == len(Q), "this method only works when P and Q have the same number of coefficients"
    n = max(len(P), len(Q))
    QQ = Q + [0 for i in range(n - len(Q))]
    PP = P + [0 for i in range(n - len(P))]
    if n==1:
        return [P[0]*Q[0]]
    n2=n//2
    P0=[PP[i] for i in range(n2)]
    P1=[PP[i] for i in range(n2,n)]
    Q0=[QQ[i] for i in range(n2)]
    Q1=[QQ[i] for i in range(n2,n)] 
    A=poly_kara_mult(P0,Q0)
    B=poly_kara_mult(P1,Q1)    
    C=poly_kara_mult(poly_add(P0,P1),poly_add(Q0,Q1))
    D=poly_add(poly_add(C,neg(A)),neg(B))
    return poly_add(poly_add(A,shift(D,n2)),shift(B,2*n2))[:n - 1 + min(len(P), len(Q))]


def split(A):
    row, col = len(A), len(A[0])
    row2, col2 = row//2, col//2
    return [A[i][:col2] for i in range(row2)], [A[i][col2:] for i in range(row2)], [A[i][:col2] for i in range(row2,row)], [A[i][col2:] for i in range(row2,row)]

def merge(a,b,c,d):
    return list(map(lambda e : e[0]+e[1], zip(a,b))) + list(map(lambda e : e[0]+e[1], zip(c,d)))

def add_matrix_pol(A,B):
    n = len(A)
    C = [[[0] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = poly_add(A[i][j], B[i][j])
    return C

def sub_matrix_pol(A,B):
    n = len(A)
    C = [[[0] for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = poly_add(A[i][j], neg(B[i][j]))
    return C

def strassen_kara(A,B):
    n = len(A)
    if n == 1:
        temp = poly_kara_mult(A[0][0],B[0][0])
        return [[temp]]
    a, b, c, d = split(A)
    x, y, z, t = split(B)
    q1 = strassen_kara(a, add_matrix_pol(x,z)) 
    q2 = strassen_kara(d, add_matrix_pol(y,t))       
    q3 = strassen_kara(sub_matrix_pol(d,a), sub_matrix_pol(z,y))       
    q4 = strassen_kara(sub_matrix_pol(b,d), add_matrix_pol(z,t))       
    q5 = strassen_kara(sub_matrix_pol(b,a), z)       
    q6 = strassen_kara(sub_matrix_pol(c,a), add_matrix_pol(x,y)) 
    q7 = strassen_kara(sub_matrix_pol(c,d), y) 
    c11 = add_matrix_pol(q1,q5) 
    c12 = add_matrix_pol(add_matrix_pol(q2,q3),sub_matrix_pol(q4,q5))          
    c21 = add_matrix_pol(add_matrix_pol(q1,q3),sub_matrix_pol(q6,q7))          
    c22 = add_matrix_pol(q2,q7)
    c = merge(c11,c12,c21,c22)
    return c


def mult_matrix_vector_poly(v,Mi):
    n = len(Mi)
    w = [[0] for i in range(n)]
    for i in range(n):
        for j in range(n):
            w[i] = poly_add(w[i], poly_mult(v[j], Mi[j][i]))
    return w

def mult_matrix_vector(v,Mi):
    n = len(Mi)
    w = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            w[i] += v[j] * Mi[j][i]
    return w

""" Modify after this line """

# Question 6

def MV_vectors(M):
    pass

def MV_PIT(M):
    pass

# Question 7

# Question 8

# Question 9

def MM_matrix(M):
    pass

def MM_matrix(M):
    pass

# Question 10

# Question 11

# Question 12

def eval_MV_PIT(M,p):
    pass

# Question 13

# Question 14

def MC_eval_PIT(M,S):
    pass
