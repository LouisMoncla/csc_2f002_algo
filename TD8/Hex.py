# -*- coding: utf-8 -*-

from uf import Rank_UF

import random

class Hex:
    def __init__(self, N):
        # size of the board (counting extra rows / columns)
        self.size = N+2
        # initialisation of the board (all hexagons are free)
        self.board = [[0 for j in range(self.size)] for i in range(self.size)]

        # initialisation of the Union-Find object
        nelem = self.size**2
        self.uf = Rank_UF(nelem)

        # first player to play is player 1
        self.player = 1


        l = self.size-1
        # union of sides of each player
        # player 1 is affected to the extra rows, player 2 extra columns
        for i in range(1,self.size-1):
            self.board[0][i] = 1
            self.board[l][i] = 1
            self.board[i][0] = 2
            self.board[i][l] = 2


            if i > 0:
                self.uf.union(self.hex_to_int(1,0), self.hex_to_int(i,0))
                self.uf.union(self.hex_to_int(1,l), self.hex_to_int(i,l))

                self.uf.union(self.hex_to_int(0,1), self.hex_to_int(0,i))
                self.uf.union(self.hex_to_int(l,1), self.hex_to_int(l,i))

        # get the indices in UF of the bottom and top sides of each player
        self.bot = [-1, self.hex_to_int(0,1), self.hex_to_int(1,0)]
        self.top = [-1, self.hex_to_int(l,1), self.hex_to_int(1,l)]

    def hex_to_int(self, i, j):
        return i*(self.size) +j

    def print_board(self):
        for i in range(1, self.size-1):
            print(' '*(i-1),end='')
            for j in range(1, self.size-1):
                if self.board[i][j] == 0:
                    print('_', end='')
                if self.board[i][j] == 1:
                    print('X', end='')
                if self.board[i][j] == 2:
                    print('O', end='')
            print()


    def neighbours(self, i, j):
        #TO IMPLEMENT
        #liste des voisins a tester
        voisins=[(i, j+1), (i, j-1), (i+1, j), (i-1, j), (i-1, j+1), (i+1, j-1)]
        # le joueur actuel 1 ou 2
        player= self.player
        #liste des hexagones qui belong au joueur actuel
        belong= []
        for i, j in voisins:
            if 0<=j<self.size and 0<=i<self.size:
                if self.board[i][j] == player:
                    belong.append([i, j])

        return belong


        
    
    def is_game_over(self):
        #TO IMPLEMENT
        player=self.player
        return self.uf.is_connected(self.top[player], self.bot[player])
    
    


    def random_turn(self):
        #TO IMPLEMENT
        player = self.player 
        choice = 1
        while choice!=0:
            i , j = random.randint(1, self.size-2), random.randint(1, self.size-2)
            choice = self.board[i][j]
        self.board[i][j]=player
        for p, q in self.neighbours(i, j):
            self.uf.union(self.hex_to_int(i,j), self.hex_to_int(p, q))

        # Connect to the appropriate borders
        if player == 1:
            if i == 1:
                self.uf.union(self.hex_to_int(i, j), self.top[1])
            if i == self.size-2:
                self.uf.union(self.hex_to_int(i, j), self.bot[1])

        else:
            if j == 1:
                self.uf.union(self.hex_to_int(i, j), self.bot[2])
            if j == self.size-2:
                self.uf.union(self.hex_to_int(i, j), self.top[2])

        self.player = 3 - player
        


    def random_play(self):
        #TO IMPLEMENT
        count=0
        while not self.is_game_over():
            self.random_turn()
            count+=1

        self.print_board()
        return count/(self.size-2)**2