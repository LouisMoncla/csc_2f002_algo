# -*- coding: utf-8 -*-

import math

def binary_search_rec(A,v,left,right):
    if (right >= left):
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            return binary_search_rec(A,v,left,mid-1)
        else:
            return binary_search_rec(A,v,mid+1,right)
    
    return -1
        
## Q1 ##
def binary_search(A,v):
    n=len(A)
    left = 0
    right = n-1
    while left<=right :
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            right = mid -1
        else:
            left = mid +1
    return -1 
        
def cost_binary_search(n):
    if n==0: return 1
    if n==1 : return 4
    return cost_binary_search((n+1)//2)+3
    
## Q2 ##
def ternary_search(A,v):
    n = len(A)
    l=0
    r=n-1
    while l<=r:
        m1= l + (r-l)//3
        m2= r - (r-l)//3
        if v==A[m1]: return m1
        elif v==A[m2]: return m2
        elif v < A[m1]: 
            r=m1 -1
        elif v > A[m2]:
            l=m2 +1
        else: 
            l=m1 +1
            r=m2 -1
        
    return -1

def cost_ternary_search(n):
    if n==0 : return 1
    if n==1: return 4
    return cost_ternary_search((n+2)//3) + 4
    
def cost_binary_search_value(A,v):
    # if len(A) == 0: return 1
    left = 0
    right = len(A) - 1

    cost = 1
    while (right >= left):
        mid = left + (right - left)//2
        cost += 1 
        if (v == A[mid]):
            return cost
        else: # decomposed elif into else if, then inserted "cost += 1" before the if
            cost += 1
            if (v < A[mid]):
                right = mid - 1
            else:
                left = mid + 1
        cost += 1

    return cost

def cost_ternary_search_value(A,v):
    n= len(A)
    l = 0
    r = n - 1

    cost = 1
    while (l<=r):
        m1= l + (r-l)//3
        m2= r - (r-l)//3
        
        cost+=1
        if v == A[m1]:
            return cost
        
        cost+=1
        if  v==A[m2]:
            
            return cost
        cost+=1
        if (v < A[m1]):
            r = m1-1

        else: 
            cost+=1
            if (v > A[m2]):
                l = m2 +1
            else: 
                l=m1 +1
                r=m2 -1
        cost+=1 #the loop

    return cost

## Q3 ##
def binary_search_bis(A,v, left, right):
    n=len(A)
    while left<=right :
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            return mid
        elif (v < A[mid]):
            right = mid -1
        else:
            left = mid +1
    return -1 


def exponential_search(A,v):
    n=len(A)
    l=0
    r=n-1
    k=0
    while True:
        index=2**k
        if index>=n:
            l=index//2
            break
        if A[index]>v:
            r= index
            l=index//2
            break

        k+=1
    return binary_search_bis(A,v,l,r)
        

def cost_exponential_search(v):
    if v <= 0 :
        K = 0
    else: 
        K= math.floor(math.log2(v))+1
    cost=K+1
    plage=2**(K-1)+1
    if K>=1:
        return 2*cost + cost_binary_search(plage)
    if K==0: 
        return 2*cost + cost_binary_search(2)



## Q4 ##
def interpolation_search(A,v):
    n= len(A)
    l=0
    r=n-1

    while l<=r:
        if A[r]==A[l] :
            if A[l]==v:
                return l
            else : break
        if A[l]>v or A[r]<v: break
        k= l + ((v - A[l])*(r-l))//(A[r]-A[l])
        if A[k]==v: return k
        elif A[k]>v:
            r=k-1
        else:
            l=k+1

    return -1

## Q6 ##

def findFirstOccurrence(A, v):
    n=len(A)
    left = 0
    right = n-1
    index = -1
    while left<=right :
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            index = mid
            right = mid - 1 
        elif (v < A[mid]):
            right = mid -1
        else:
            left = mid +1
    return index

def findLastOccurrence(A, v):
    n=len(A)
    left = 0
    right = n-1
    index = -1
    while left<=right :
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            index = mid
            left = mid +1
        elif (v < A[mid]):
            right = mid -1
        else:
            left = mid +1
    return index


## Q7 ##
def findKClosestElements(A, v, k):
    index= -1
    n=len(A)
    left = 0
    right = n-1
    while left<=right :
        mid = left + (right - left)//2 # using `(right + left)//2` can lead to an integer overflow
        if (v == A[mid]):
            index=mid
            break
        elif (v < A[mid]):
            right = mid -1
        else:
            left = mid +1
    

    if index==-1:
        index=left
    
    gauche=index
    droite=index-1

    for i in range(k):
        if gauche-1 <0:
            droite+=1
        elif droite+1>=n:
            gauche-=1
        elif v-A[gauche-1]<=A[droite+1]-v:
            gauche-=1
        else : 
            droite+=1
    return A[gauche:droite+1]

## Q8 ##
def findFrequency(A):
    retour = dict ()
    n=len(A)
    marqueur=0
    while marqueur<n :
        index = findLastOccurrence(A, A[marqueur])
        retour [A[marqueur]]= index +1 - marqueur
        marqueur= index +1
    return retour 
