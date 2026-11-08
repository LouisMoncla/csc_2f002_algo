# Question 1
def middleL(n, i, j, a, b): # returns the middle of the punctured grid of type (n, i, j, a, b)
    if n==0 : return 
    retour=[
        (i+2**(n-1)-1, j+2**(n-1)-1), 
        (i+2**(n-1)-1, j+2**(n-1)), 
        (i+2**(n-1), j+2**(n-1)-1), 
        (i+2**(n-1), j+2**(n-1))
    ]

    
    if a<i+2**(n-1):
        if b<j+2**(n-1):
            retour.remove((i+2**(n-1)-1, j+2**(n-1)-1))
        else :
            retour.remove((i+2**(n-1)-1, j+2**(n-1)))
    else:
        if b<j+2**(n-1):
            retour.remove((i+2**(n-1), j+2**(n-1)-1))
        else:
            retour.remove((i+2**(n-1), j+2**(n-1)))
    
    return retour
    

# Question 2
def lower_left_hole(n, i, j, a, b): # returns the coordinates of the hole of the lower left quadrant
    if a<i+2**(n-1) and b<j+2**(n-1):
        return (a, b)
    return i+2**(n-1)-1, j+2**(n-1)-1

def lower_right_hole(n, i, j, a, b): # returns the coordinates of the hole of the lower right quadrant
    if a>i+2**(n-1)-1 and b<j+2**(n-1):
        return (a, b)
    return i+2**(n-1), j+2**(n-1)-1

def upper_left_hole(n, i, j, a, b): # returns the coordinates of the hole of the upper left quadrant
    if a<i+2**(n-1) and b>j+2**(n-1)-1:
        return (a, b)
    return i+2**(n-1)-1, j+2**(n-1)

def upper_right_hole(n, i, j, a, b): # returns the coordinates of the hole of the upper right quadrant
    if a>=i+2**(n-1) and b>=j+2**(n-1):
        return (a, b)
    return i+2**(n-1), j+2**(n-1)

# Question 3
def tile(n, i, j, a, b): # returns a list with a valid L-tiling of the punctured grid of type (n, i, j, a, b)
    tilling=[]
    #Base case
    if n==1: 
        tilling.append(middleL(n, i, j, a, b))
        return tilling
    
    k, l = lower_left_hole(n, i, j, a, b)
    low_left= tile (n-1, i, j, k, l)
    
    k, l =  lower_right_hole(n, i, j, a, b)
    low_right= tile (n-1, i+2**(n-1), j, k, l)
    
    k, l = upper_left_hole(n, i, j, a, b)
    up_left= tile (n-1, i, j+2**(n-1), k, l )
    
    k, l = upper_right_hole(n, i, j, a, b)
    up_right= tile (n-1, i+2**(n-1), j+2**(n-1), k, l)

    return low_left+low_right+up_right+up_left+[middleL(n, i, j, a, b)]
