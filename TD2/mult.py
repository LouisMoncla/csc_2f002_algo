# -*- coding: utf-8 -*-

# Q1

def poly_mult(P,Q):
    # I put i and P together and Q and j
    degP=len(P)
    degQ=len(Q)
    
    retour=[0 for i in range(degP+degQ-1)]
    
    for i in range (len(P)):
        for j in range (len(Q)):
            retour[i+j]+= P[i]*Q[j]

    return retour


def cost_poly_mult(n): 
    return 2*n**2-2*n+1

# Q2

def poly_add(P,Q):
    if len(P)<len(Q):
        P, Q= Q, P
    R=P[:]
    for i in range (len(Q)):
         R[i]+=Q[i]
    return R

         
def neg(P):
    return [-p for p in P]

   
def shift(P,k):
   decallage=[0 for i in range (k)]
   return decallage+P
  
# Q3  
  
def poly_kara_mult(P,Q):
    n=len(P)
    if n<=2:
        return poly_mult(P, Q)
    k=(n+1)//2
    P0=P[:k]
    P1=P[k:]
    Q0=Q[:k]
    Q1=Q[k:]
    H0=poly_kara_mult(P0,Q0)
    H2=poly_kara_mult(P1,Q1)
    H1tilde=poly_kara_mult(poly_add(P0,P1),poly_add(Q0,Q1))
    negH0= neg(H0)
    negH2= neg(H2)
    H1tildenegH0negH2 = poly_add( H1tilde , poly_add( negH0, negH2) )
    retour = poly_add(H0, poly_add( shift(H1tildenegH0negH2, k), shift( H2 , 2*k) ) )
    return retour

    
def cost_poly_kara_mult(n):
    if n==1 : return 1
    return 3*cost_poly_kara_mult((n+1)//2)+4*n

# Q4 

def cost_poly_tc3_mult(n):
    if n == 1 : return 1
    if n == 2 : return 3
    return 5 * cost_poly_tc3_mult((n+2)//3) + 30 * n

# Q5 hybrid
   
def poly_switch_mult(d,P,Q):
    n=len(P)
    if n<=d:
        return poly_mult(P, Q)
    k=(n+1)//2
    P0=P[:k]
    P1=P[k:]
    Q0=Q[:k]
    Q1=Q[k:]
    H0=poly_switch_mult(d, P0, Q0)
    H2=poly_switch_mult(d, P1, Q1)
    H1tilde=poly_switch_mult(d, poly_add(P0,P1), poly_add(Q0,Q1))
    negH0= neg(H0)
    negH2= neg(H2)
    H1tildenegH0negH2 = poly_add( H1tilde , poly_add( negH0, negH2) )
    retour = poly_add(H0, poly_add( shift(H1tildenegH0negH2, k), shift( H2 , 2*k) ) )
    return retour
    

def cost_switch_mult(d,n):
    if n<=d:
        return 2*n**2-2*n+1
    return 3*cost_switch_mult(d, (n+1)//2) +4*n 

   
