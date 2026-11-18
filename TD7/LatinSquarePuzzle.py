# -*- coding: utf-8 -*-

try:
    from Sat import *
except Exception:
    pass

class LatinSquarePuzzle:
    def __init__(self,k,initial):
      self.k=k  
      self.initial=initial
      self.sat=Sat(self.k**3,[])   
      self.final=[]
        
    def triple_to_int(self,v,i,j):
        return (i*self.k + j)*self.k + v + 1
        
    def int_to_triple(self,r):
        temp = r - 1
        v = temp % self.k

        temp //= self.k
        j = temp % self.k

        temp //= self.k
        i = temp % self.k

        return [v,i,j]

    # Question 3
    
    def build_generic_clauses(self):
        # TO COMPLETE
        for i in range (self.k):
            for j in range (self.k):
                clause=[]
                for v in range(self.k):
                    clause.append(self.triple_to_int(v, i, j))
                self.sat.clauses.append(clause)
                for v1 in range(self.k):
                    for v2 in range(v1+1, self.k):
                        clause=[-self.triple_to_int(v1, i , j), -self.triple_to_int(v2, i , j)]
                        self.sat.clauses.append(clause)

        for v in range (self.k):
            for i in range (self.k):
                clause=[]
                for j in range(self.k):
                    clause.append(self.triple_to_int(v, i, j))
                self.sat.clauses.append(clause)
                for j1 in range(self.k):
                    for j2 in range(j1+1, self.k):
                        clause=[-self.triple_to_int(v, i , j1), -self.triple_to_int(v, i , j2)]
                        self.sat.clauses.append(clause)

        for v in range (self.k):
            for j in range (self.k):
                clause=[]
                for i in range(self.k):
                    clause.append(self.triple_to_int(v, i, j))
                self.sat.clauses.append(clause)
                for i1 in range(self.k):
                    for i2 in range(i1+1, self.k):
                        clause=[-self.triple_to_int(v, i1 , j), -self.triple_to_int(v, i2, j)]
                        self.sat.clauses.append(clause)
        

    # Question 4
    
    def add_fixed_value_clauses(self):
        # TO COMPLETE
        for i in range(self.k):
            for j in range(self.k):
                coef= self.initial[i][j] 
                if coef!='*':
                    clause=[self.triple_to_int(coef, i, j)]
                    self.sat.clauses.append(clause)

    
    # Questions 5 & 8
    
    def solve(self, propagation=False):
        # TO COMPLETE
        n=self.k**3
        R = 4*n**2
        self.build_generic_clauses()
        self.add_fixed_value_clauses()
        if propagation is True:
            self.sat.simplify_formula_by_propagation()
            f= n - len(self.sat.fixed)
            if f==0: return
            R = 4*f**2
            
        self.sat.walk_sat(R)
        for i in range(self.k):
            self.final.append([])
            for j in range(self.k):
                self.final[i].append(0)
                for v in range(self.k):
                    if self.sat.values[self.triple_to_int(v, i, j)]:
                        self.final[i][j]=v


         
    ##################################################
    # DISPLAY METHODS
    ##################################################      
     
    def display_before_solving(self, prefix=""):
        print(prefix + "Initial configuration:")
        for r in range(self.k): 
            print(prefix + "[{0}]".format(', '.join(map(str, self.initial[r]))))
        print("")    

    def display_after_solving(self, prefix=""):
        if(len(self.final)==0):
            print(prefix + "Not yet solved")
            return
        print(prefix + "Solved configuration:")
        for r in range(self.k):    
            print(prefix + "[{0}]".format(', '.join(map(str, self.final[r]))))
        print("")     
