#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import numpy as np


#Q6
def mult_matrix(A,B):
    n = len(A)
    C=[[0 for i in range (n) ] for i in range (n)]
    for i in range(n):
        for j in range (n):
            for k in range (n):
                C[i][j]+=A[i][k]*B[k][j]
    return C


#Q7
def cost_mult_matrix(n):
    return n*n*(2*n-1)

#Functions split, merge, add_matrix and sub_matrix are given
def split(A):
    row, col = len(A), len(A[0])
    row2, col2 = row//2, col//2
    return [A[i][:col2] for i in range(row2)], [A[i][col2:] for i in range(row2)], [A[i][:col2] for i in range(row2,row)], [A[i][col2:] for i in range(row2,row)]

def merge(a,b,c,d):
    return list(map(lambda e : e[0]+e[1], zip(a,b))) + list(map(lambda e : e[0]+e[1], zip(c,d)))

# def split(A):
#    A=np.array(A)
#    row, col = A.shape
#    row2, col2 = row//2, col//2
#    return A[:row2, :col2].tolist(), A[:row2, col2:].tolist(), A[row2:, :col2].tolist(), A[row2:, col2:].tolist()

#def merge(a,b,c,d):
#    return np.vstack((np.hstack((a, b)), np.hstack((c, d)))).tolist()

#Computes the matrix A+B
def add_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] + B[i][j]
    return C

#Computes the matrix A-B
def sub_matrix(A,B):
    n = len(A)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
                C[i][j] = A[i][j] - B[i][j]
    return C

#Q8
def strassen(A,B):
    if len(A)==1: return mult_matrix(A, B)
    a, b, c, d= split(A)
    x, y, z, t= split(B)
    q1= strassen(a, add_matrix(x, z))    
    q2= strassen(d, add_matrix(y, t))  
    q3= strassen(sub_matrix(d, a), sub_matrix(z, y))
    q4= strassen(sub_matrix(b, d), add_matrix(z, t))
    q5= strassen(sub_matrix(b, a), z)
    q6= strassen(sub_matrix(c, a), add_matrix(x, y))
    q7= strassen(sub_matrix(c, d), y)  
    return merge(add_matrix(q1, q5), add_matrix(add_matrix(q2,q3), sub_matrix(q4, q5)), add_matrix(add_matrix(q1, q3), sub_matrix(q6, q7)) ,add_matrix(q2, q7))



#Q9
def cost_strassen(k):
    if k==0: return 1
    if k==1 : return 25
    return 7*cost_strassen(k-1)+18*2**(2*k-2)


#Q10
def convert_01(A):
    n=len(A)
    E=[[0]*n for i in range(n)] 

    for i in range (n):
        for j in range(n) :
            E[i][j]= 1 if A[i][j]>0 else 0
    return E
#Q11
def transitive_closure(A):
    n= len(A)
    
    
    def Identity_n(n):
        In=[[0]*n for i in range(n)] 
        for i in range (n):
            In[i][i]= 1
        return In
    
    def or_matrix(A, B):
        n=len(A)

        E=[[0]*n for i in range(n)] 
        for i in range (n):
            for j in range(n):
                E[i][j]= A[i][j] or B[i][j]
        return E 

    def bin_pow_matrices(A, e):
        if e==0: return Identity_n(len(A))
        if e==1: return A
        tmp= bin_pow_matrices(A, e//2)
        tmp= convert_01(strassen(tmp, tmp))
        if e%2==0: return tmp
        return convert_01(strassen(A, tmp))

    
    In = Identity_n(n)

    M = convert_01(A)

    E = or_matrix( In, M)

    R = bin_pow_matrices(E, n-1)
    return R






