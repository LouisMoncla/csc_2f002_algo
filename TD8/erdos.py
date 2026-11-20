# -*- coding: utf-8 -*-

from uf import Rank_UF

import random
import math
 
def Erdos_Renyi(N):
    #TO IMPLEMENT
    G=Rank_UF(N)
    edges= 0
    while G.get_count()>1:
        p = random.randint(0, N-1)
        q = random.randint(0, N-1)
        while p==q:
            q = random.randint(0, N-1)

        if not G.is_connected(p, q):
            G.union(p, q)
        edges+=1
    return edges
    
