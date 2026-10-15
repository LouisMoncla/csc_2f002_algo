# -*- coding: utf-8 -*-

class PowerTree:
    
  # constructor, initializes the tree with a single node (the root 1)
  # and a single layer (layer 0, containing the root node)  
    def __init__(self): 
        self.layers=[[1]]
        self.parent={1:1}
    
  # displays the layers of the tree
    def draw_tree(self):
        for i in range(len(self.layers)):	
            print("layer",i)
            for j in self.layers[i]: print(j,"->",self.parent[j])  
  	
  # if k is not in the tree (not enough layers built) return -1
  # if k is in the tree, returns a list giving the successive labels
  # on the path from the root (equal to 1) to k
    def path_from_root(self,k):
      if k not in self.parent: return -1
      if k==1: return [1]
      path=[k]
      while self.parent[k]!= 1:
        path.append(self.parent[k])
        k=self.parent[k]
      path.append(1)
      return path[::-1]
            
    
  # adds the (k+1)th layer to the tree, when the layers
  # already in the tree are 0..k  
    def add_layer(self):
        self.layers.append([])
        for elem in self.layers[-2]:
          path = self.path_from_root(elem)
          for parent in path : 
            new_elem= elem+parent
            if elem+parent not in self.parent:
              self.layers[-1].append(new_elem)
              self.parent[new_elem]=elem
                

