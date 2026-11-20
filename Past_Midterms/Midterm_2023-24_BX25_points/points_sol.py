#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import math
import timeit

#Q1
def min_max_aux(A, left, right):
    if len(A) == 0: return
    if len(A) == 1 : return (A[0], A[0])
    
    #print(f'left is {left} and right is {right}')
    if right - left == 0: return (A[right], A[right])
    if right - left == 1:
        if A[left] >= A[right]:
            mini, maxi = A[right], A[left]
        else:
            mini, maxi = A[left], A[right]
        return (mini, maxi)
    middle = left + (right - left )//2
    rec1 = min_max_aux(A, left, middle)
    rec2 = min_max_aux(A, middle+1, right)
    if rec1[0] >= rec2[0]:
        mini = rec2[0]
    else:
        mini = rec1[0]
    if rec1 [1]>= rec2[1]:
        maxi = rec1[1]
    else: 
        maxi = rec2[1]
    return (mini, maxi)
    

def min_max(A):
    if len(A) == 0: return
    if len(A) == 1: return A[0]
    return min_max_aux(A, 0, len(A)-1)
    
    
# As seen in the lectures, we have the following recurrence 
#       C(0) = C(1) = 0
#       C(n) <= 2*C(ceil(n/2)) + lambda*n 
# By iterating k times such that k = ceil(log_2(n)), then
#       C(n) <=  lambda*N 
# In our code we only have a constant cost on top of the recursion which is 2. This is the number
# of comparisons we make. Hence, it is clearly less than some lamda*N. So, the complexity is less than 3/2*n.
    

# We assume that the set of points S is given as a list of 2-size lists representing the x and y coordinates of a point, respectively

#Q2
def bounding_box(S):
    x_coord = [S[i][0] for i in range(len(S))]
    y_coord = [S[i][1] for i in range(len(S))]
    minx , maxx = min_max(x_coord) 
    miny , maxy = min_max(y_coord)
    return [[minx, maxy], [maxx, miny]]
    
    

#Q3

def lexicographic(p1,p2): 
    if (p1[0] < p2[0]):
        return True
    elif (p1[0] == p2[0] ):
        return p1[1] <= p2[1]
    return False

 #helper function   
def dominate(p1, p2):
    if p2[0] >= p1[0] and p2[1] >= p1[1]:
        return True
    return False

def maxima_set(S):
    if len(S) == 1: return S
    #let's find p
    ordered_x = []
    for i in range(len(S)):
        if ordered_x == []:
            ordered_x += [S[i][0]]
        elif ordered_x[-1] > S[i][0]:
            ordered_x = [S[i][0]] + ordered_x
        elif ordered_x[-1] < S[i][0]:
            ordered_x += [S[i][0]]
        else:
            if S[i][1] > ordered_x[-1]:
                ordered_x += S[i][0]
            else: 
                ordered_x = S[i][0] + ordered_x
    #all points are in lexicographic order in ordered_x
    #we now determine the median p
    n = len(S) - 1
    p = ordered_x[n//2]
    #the median p is found
    
    S_left = [points for points in S if points[0] <= p]
    S_right = [points for points in S if points[0] > p]
    
    rec_l = maxima_set(S_left)
    rec_r = maxima_set(S_right)
    #find q
    mini_maxima = None
    for maximas in rec_r:
        if mini_maxima is None or lexicographic(maximas, mini_maxima):
            mini_maxima = maximas
    fin_rec_l = []
    for maximas in rec_l:
        if not dominate(maximas, mini_maxima):
            fin_rec_l.append(maximas)
    #define set of maximas
    set_maximas = fin_rec_l + rec_r
    return set_maximas 

#A = [[2 ,6] ,[3 ,7] ,[4 ,5] ,[6 ,4] ,[8 ,6] ,[9 ,3] ,[10 ,2] ,[11 ,2]]
#print(maxima_set(A) )  


#Q4
def min_distance(S):
    points = S
    delta = math.dist(S[0], S[1])
    changed = True
    while changed:
        #build the subdivision
        breaking = False
        subdivision = dict()
        while breaking :
            for s in range(0, 1, delta/2):
                for t in range(0, 1, delta/2):
                    for i in range(len(points)):  
                        if s <= points[i][0] <= s+delta/2 and t<= points[i][1] <= t+delta/2:
                            if (s,t) not in subdivision.keys():
                                subdivision[ (s,t) ] = i
                            else:
                                delta = math.dist( subdivision[ (s,t) ], points[i])
                                breaking = True
                                break
                    breaking = False
                if breaking:
                    break
            if breaking:
                break
            
            
        #subdivision is built
        #let's build the close set 
              
        #close = dict()              
        for i in range(len(points)):
            for key, values in subdivision.items():
                if values == i:
                    square = key
            for j in range(len(points)):
                if j != i:
                    #find (s', t')
                    for key, values in subdivision.items():
                        if values == j:
                            square_close = key
                            if math.abs(square[0] - square_close[0]) <= 2 and math.abs(square[1] - square_close[1]) <= 2:
                                delta_bis = math.dist(points[subdivision[square]], points[subdivision[square_close]])
                                if delta_bis < delta:
                                    changed = True
                                    break
                                changed = False
                if changed:
                    break
            if changed:
                break
                        
    return delta 


            





