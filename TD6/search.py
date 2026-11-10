# -*- coding: utf-8 -*-

### For comparing strings

def string_compare(P,S):
    for j in range(len(P)):
        if not P[j] == S[j]:
            return False
    return True


### naive string matcher
def string_match(T, P):
    match=[]
    m=len(P)
    for i in range (len(T)):
        if T[i:i+m] == P :
            match.append(i)
    return match

### number of characters
base = 256

### karp_rabin_sum

def hash_string_sum(S):
    somme=0
    for char in S:
        somme+=ord(char)
    return somme

def hash_string_sum_update(h, Ti, Tim):
    return h-ord(Ti)+ord(Tim)

def karp_rabin_sum(T,P):
    spurious = 0 #wrong matches
    m=len(P) # longueur du string dont on cherche les apparitions 
    match=[] # liste des coordonnes du debut des matchs
    n=len(T) #longueur du string 
    h= hash_string_sum(P) #le hash de P longueur m 
    T_i= hash_string_sum(T[:m]) # le hash de T d'index 0 a m-1
    for i in range(n-m+1):
        if h==T_i: 
            if string_compare(P,T[i:i+m]):
                match.append(i)
            else: 
                spurious+=1
        if i < n-m:
            T_i = hash_string_sum_update(T_i, T[i], T[i+m])
    return (match, spurious)



### karp_rabin_mod

def hash_string_mod(S, q):
    m=len(S)
    d=256
    sum=ord(S[0])
    for i in range(m-1):
        sum=sum*d+ord(S[i+1])
       
    return sum%q

def hash_string_mod_update(h, Ti, Tim, q, dm):
    return (256*(h-dm*ord(Ti))+ord(Tim))%q

def karp_rabin_mod(T,P, q):
    spurious = 0 #wrong matches
    m=len(P) # longueur du string dont on cherche les apparitions 
    match=[] # liste des coordonnes du debut des matchs
    n=len(T) #longueur du string 
    h= hash_string_mod(P, q) #le hash de P longueur m 
    T_i= hash_string_mod(T[:m], q) # le hash de T d'index 0 a m-1
    dm=(256**(m-1))%q
    for i in range(n-m+1):
        if h==T_i: 
            if string_compare(P,T[i:i+m]):
                match.append(i)
            else: 
                spurious+=1
        if i < n-m:
            T_i = hash_string_mod_update(T_i, T[i], T[i+m], q, dm)
    return (match, spurious)