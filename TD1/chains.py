# -*- coding: utf-8 -*-

import math
try:
    from PowerTree import *
except:
    pass

## Q1 ##

# binary powering, returns x^n
def bin_pow(x, n):
    if n==0: return 1
    if n==1: return x
    tmp= bin_pow(x, n//2)
    tmp*= tmp
    if n%2==0: return tmp
    return x*tmp

## Q2 ##

# returns the number of multiplications of a call to
# bin_pow(x,n)
def cost_bin_pow(n):
    if n == 1 or n == 0: return 0
    if n%2==0: return 1+ cost_bin_pow(n//2)
    return 2 + cost_bin_pow(n//2)

## Q3 ##

# returns -1 if n is prime, and returns the smallest factor
# p>=2 of n if n is composite
def smallest_factor(n):
    for i in range(2, int((abs(n)**0.5))+1):
        if n%i==0: return i
    return -1


## Q4 ##

# factorization powering, returns x^n
def factor_pow(x, n):
    if n==0: return 1
    if n==1: return x
    p=smallest_factor(n)
    if p==-1: return x*factor_pow(x, n-1)
    return factor_pow(factor_pow(x, p), n//p)
## Q5 ##

# returns the number of multiplications of a call to
# factor_pow(x,n)
def cost_factor_pow(n):
    if n==0 or n==1: return 0 
    p=smallest_factor(n)
    if p==-1: return 1+cost_factor_pow(n-1)
    return cost_factor_pow(p)+ cost_factor_pow(n//p)


## Q6 ##

# returns x^n from an addition chain of n (stored in the parameter chain)
def power_from_chain(x, chain):
    L=dict()
    L[chain[0]]=x
    for k in range(1, len(chain)): 
        j=chain[k]-chain[k-1]
        L[chain[k]]=L[chain[k-1]]*L[j]
    return L[chain[-1]]


## Q8 ##

# returns the addition chain for n (path from the root
# to n in the power tree) after inserting enough
# layers of the tree so that n is part of it
def power_tree_chain(n):
    P=PowerTree()
    while n not in P.parent:
        P.add_layer()
    return P.path_from_root(n)

# power tree powering, returns x^n
def power_tree_pow(x, n):
    if n == 0: return 1
    L = power_tree_chain(n)
    return power_from_chain(x, L)

## Q9 ##

# number of multiplications of a call to power_tree_pow(x,n)
# does not count the cost of building the tree
def cost_power_tree_pow(n):
    if n <= 1:
        return 0
    return len(power_tree_chain(n)) - 1

# prints the compared costs
def compare_costs(N=40):
    for n in range(N + 1):
        print(f"n = {n}")
        print(f"  bin_pow cost:    {cost_bin_pow(n)}")
        print(f"  factor_pow cost: {cost_factor_pow(n)}")
        print(f"  power_tree cost: {cost_power_tree_pow(n)}")