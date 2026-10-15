# -*- coding: utf-8 -*-

### Question 1 ###
def peak_naive(L):
    n=len(L)
    
    for i in range(1, L):
        if L[i]>=L[i-1] and L[i]<=L[i+1]:
            return i


### Question 2 ###   
def peak(L):    
    # TO IMPLEMENT
    pass
    
def peak_aux(L,p,q):    
    # TO IMPLEMENT
    pass    
    
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
