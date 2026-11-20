# -*- coding: utf-8 -*-

class UF_base:
    '''
        basic Union-Find implementation, implementing Quick-find
    '''
    def __init__(self, N):
        self.N = N  # number of elements
        self.A = [i for i in range(N)]  #Array representing the forest
        self.count = N   # number of equivalence classes, i.e. the number of trees in the forest
    
    def get_N(self):
        return self.N
        
    def get_count(self):
        return self.count
    
    def union(self,p,q):
        if self.is_connected(p,q):
            return

        # merging the classes of p and q
        self.count -= 1            
        r1 = self.find(p)
        r2 = self.find(q)
        
        # all the elements with root r2 now has root r1
        for i in range(self.N):
            if self.A[i] == r2:
                self.A[i] = r1
        
    def find(self, p):
        return self.A[p]
            
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Rank_UF(UF_base):
    def __init__(self,N):
        super().__init__(N)
        self.rank = [1 for _ in range(N)]
        
    def find(self, p):
        # TO IMPLEMENT
        #path compression
        to_compress = [p]
        fiston = p
        root = None
        while root is None:
            #fenetre glissante
            parent = self.A[fiston]
            if parent == fiston:
                root= parent
                for elem in to_compress:
                    self.A[elem]=root
                return self.A[p]
            else: 
                to_compress.append(parent)
                fiston = parent
        return self.A[p]

        
    def union(self, p, q):
        #TO IMPLEMENT
        p = self.find(p)
        q = self.find(q)

        if self.rank[p]>self.rank[q]:
            self.A[q]= p
        elif self.rank[p]==self.rank[q]:
            self.A[q]=p
            self.rank[p]+=1
        else: 
            self.A[p]= q
        self.count-=1