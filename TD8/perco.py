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
        if  G[i][j+1]:
            vacant.append([p, q])
    return vacant 
    

def make_vacant(UF, G, N, i, j):
    '''
        TO IMPLEMENT
    '''
    pass


def ratio_to_percolate(N):
    '''
        TO IMPLEMENT
    '''
    pass
