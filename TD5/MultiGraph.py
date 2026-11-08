import math
import random

## Question 5 ##


def random_element(dict):
    card= sum(dict.values())
    key = []
    inter = []
    tot=0
    for k , v in dict.items():
        tot+=v
        key.append(k)
        inter.append(tot/card)
    x = random.random()
    for i in range(len(inter)):
        if x<inter[i]:
            return key[i]
        else:
            continue
    return key[-1]


## Question 7 ##


def random_cut(m):
    n=len(m.adj)
    partition = {x: [] for x in m.adj} #initialisation of the dict for the absorbed vertices
    for p in range (0, n-2):
        i, j = m.random_edge()
        m.contract(i , j)
        partition[i]+= [j] + partition[j]
        del partition[j]
    for k , v in m.adj.items():
        return [m.deg[k], [k]+partition[k]]


def mincut_karger(L, p):  # p is the desired error bound
    m=MultiGraph(L)
    n=len(m.deg)
    best=None
    for k in range(math.ceil(math.log(p)/ math.log(1 - 2/(n*(n - 1))))):
        m=MultiGraph(L)
        cut = random_cut(m)
        if best ==None: best = cut
        elif cut[0]<best[0]:
            best = cut
        else :
            continue
    return best

## Contains Questions 4 and 6 ##


class MultiGraph:
    def __init__(self, L):
        self.adj = {}
        self.deg = {}
        for x in L[1]: # x is a list of 3 elements, two vertices and the number of edges between them
            if x[0] not in self.adj:
                self.adj[x[0]] = {x[1]: x[2]}
                self.deg[x[0]] = x[2]
            else:
                self.adj[x[0]][x[1]] = x[2]
                self.deg[x[0]] += x[2]
            if x[1] not in self.adj:
                self.adj[x[1]] = {x[0]: x[2]}
                self.deg[x[1]] = x[2]
            else:
                self.adj[x[1]][x[0]] = x[2]
                self.deg[x[1]] += x[2]

    # i is an integer between 1 and 2^n - 2, with n the number of vertices
    def subset_from_integer(self, i):
        subset = {}
        for x in self.adj:
            if i % 2 == 1:
                subset[x] = True
            i = i >> 1
        return subset

    def cutsize(self, i):  # i is an integer between 1 and 2^n - 2, with n the number of vertices
        subset = self.subset_from_integer(i)
        res = 0
        for x, y in self.adj.items():
            for t, u in y.items():
                if x in subset and not t in subset:
                    res += u
        return [res, [x for x in subset]]

    def display(self):
        for x, y in self.adj.items():
            print("Neighbors of " + str(x) +
                  ", which has degree " + str(self.deg[x]))
            for t, u in y.items():
                print(str(t) + " with multiplicity " + str(u))

    ## Question 4 ##
    def contract(self, i, j):  # contracts edge i, j (i absorbs j)
        for neighbor, edges in self.adj[j].items():
            if neighbor != i: 
                if neighbor in self.adj[i]:
                    self.adj[i][neighbor]+=edges
                    self.adj[neighbor][i]+=edges
                    self.deg[i]+=edges
                    
                else:
                    self.adj[i][neighbor]=edges
                    self.adj[neighbor][i]=edges
                    self.deg[i]+=edges

                del self.adj[neighbor][j]
            else: 
                continue

        self.deg[i]-=self.adj[i][j]
        del self.adj[i][j]
        del self.deg[j]
        del self.adj[j]


    ## Question 6.1 ##
    def random_vertex(self):
        return random_element(self.deg)

    ## Question 6.2 ##
    def random_edge(self):
        i = self.random_vertex()
        return i, random_element(self.adj[i])
