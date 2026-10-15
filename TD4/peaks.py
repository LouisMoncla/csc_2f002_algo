# -*- coding: utf-8 -*-

### Question 1 ###
def peak_naive(L):
    n=len(L)
    if n==1: return 0
    if n==2 :
        return 0 if L[0]>=L[1] else 1
    for i in range(1, n-1):
        if L[i]>=L[i-1] and L[i]>=L[i+1]:
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
    # TO IMPLEMENT
    pass
    
### Question 4 ###
def peak2d_naive(M):
    # TO IMPLEMENT
    pass

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
