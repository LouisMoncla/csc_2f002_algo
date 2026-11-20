# -*- coding: utf-8 -*-

from uf import Rank_UF

import random

def draw_grid(grid, N):
    for ii in range(N):
        i = ii+1
        for j in range(N):
            if not grid[i][j]:
                print('X', end='')
            else:
                print(' ', end='')
        print()

def pos_to_int(N, i, j):
    return N*i+j


def get_vacant_neighbors(G,N,i,j):
    #TO IMPLEMENT
    #Graph = Rank_UF(N)
    #the pos in the graph G[i][j]
    voisins=[(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    vacant=[]
    for p, q in voisins:
        if 0<=p<N and 0<=q<N:
            if  G[p][q]:
                vacant.append([p, q])
    return vacant 
    

def make_vacant(UF, G, N, i, j):
    #TO IMPLEMENT
    #set the position to vacant
    
    G[i][j]=True
    voisins=[(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    for p, q in voisins:
            if 0<=p<N+2 and 0<=q<N:
                if  G[p][q]:
                    UF.union(pos_to_int(N, i, j), pos_to_int(N, p, q))


def ratio_to_percolate(N):
    #TO IMPLEMENT
    Grid=[[]for i in range(N+2)]
    vacant_count= 0 
    for i in range(N+2):
        for j in range(N):
            if i==0 or i==N+1:
                Grid[i].append(True)
            else:
                Grid[i].append(False)
    UF =  Rank_UF(N*(N+2))
    for j in range(N-1):
        UF.union(pos_to_int(N, 0, j), pos_to_int(N, 0, j+1))
    for j in range(N-1):
            UF.union(pos_to_int(N, N+1, j), pos_to_int(N, N+1, j+1))

    while not UF.is_connected(pos_to_int(N, 0, 0), pos_to_int(N, N+1, 0)):
        i, j = random.randint(1, N), random.randint(0, N-1)
        if not Grid[i][j]:
            make_vacant(UF, Grid, N, i, j)
            vacant_count+=1
    return vacant_count/(N**2)

    


