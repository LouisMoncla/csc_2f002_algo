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
    index_pairs=set()
    values=dict()
    ## first index pairs
    if q-p==1: 
        Apq={p}
    else:
        l=(p+q)//2
        Apq={p, l-1, l, q-1}
    for elem in Apq:
        for j in range (r, s):
            index_pairs.add((elem, j))
    #second index pairs
    if s-r==1:
        Ars={r}
    else:
        l=(r+s)//2
        Ars={r, l-1, l, s-1}
    for elem in Ars:
        for i in range(p, q):
            index_pairs.add((i, elem))

    # pair with highest value
    for (i, j) in index_pairs:
        values[(i, j)]= M[i][j]
    return max(values, key=values.get)

### Question 6 ###
def peak2d(M):    
    return peak2d_aux(M, 0, len(M), 0, len(M[0]))
  
def peak2d_aux(M,p,q,r,s):
    # outer frame
    def outer_frame(M, p, q, r, s):
        border=[]
        for j in range(s):
            border.append((p, j))
            border.append((q-1, j))
        for i in range (1, q):
            border.append((i, r)) 
            border.append((i, s-1)) 
        return border
    
    
    (i, j) = pivot(M,p,q,r,s) 
    # M[p:q][r:s] is a valid subM, pivot(M,p,q,r,s) is its pivot
    if q-p<=4 or s-r<=4: #base case
        return pivot(M,p,q,r,s) 

    elif is_peak(M, i, j):
        return (i, j)
    
    else:
        l=(p+q)//2
        m=(r+s)//2
        #4submatrices=[M[p : l][r : m], M[p : l][m : s], M[l : q][r : m], M[l : q][m : s]]
        coints=[(p, l, r, m), (p, l, m, s), (l, q, r, m), (l, q, m, s)]
        for p, q, r, s in coints:
            if (i, j) in outer_frame(M, p, q, r, s):
                return peak2d_aux(M,p,q,r,s)
    """
        #z is the max value over all entries of the outer frame
        values=dict()
        for i, j in border:
            values[(i, j)]= M[i][j]
        z= max(values.values())
    
        # Valid submatrix: all exterior neighbors are smaller
        for i, j in border:
            test=[(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for (a, b) in test:
                if a>=0 and a<I and b>=0 and r<J:
                    if a<r and a>=s and b<p and b>=q:
                        if not(M[a][b]>z) :
                            #submatrix is not good
                            pass
        """