# -*- coding: utf-8 -*-

### Question 1 ###
def peak_naive(L):
    n=len(L)
    for i in range (n-1):
        if L[i]>=L[i+1]:
            return i
    return n-1


### Question 2 ###   
def peak(L):
    return peak_aux(L, 0, len(L))
    
def peak_aux(L,p,q):    
    if q-p==1: return p

    mid= (p+q)//2

    if L[mid-1]>=L[mid]:
        if p==mid-1 or L[mid-1]>= L[mid-2]:
            return mid-1
        return peak_aux(L, p, mid)

    else: 
        if q==mid+1 or L[mid]>=L[mid+1]:
            return mid
        return peak_aux(L, mid, q)
    
    
### Question 3 ###
def is_peak(M,i,j):
    I=len(M)
    J=len(M[i])
    test=[(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
    for (r, c) in test:
        if r>=0 and r<I and c>=0 and c<J:
            if not(M[i][j]>=M[r][c]):
                return False
    return True 
    
### Question 4 ###
def peak2d_naive(M):
    I= len(M)
    J= len(M[0])
    for i in range(I):
        for j in range(J):
            if is_peak(M, i, j):
                return (i, j)

### Question 5 ###
def pivot(M,p,q,r,s):    
    # TO IMPLEMENT
    pass
    
### Question 6 ###
def peak2d(M):    
    # TO IMPLEMENT
    pass
  
def peak2d_aux(M,p,q,r,s):
    # TO IMPLEMENT
    pass    
