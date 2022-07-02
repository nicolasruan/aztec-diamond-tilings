# aztec-diamond-tilings
The module 'partitions.py' implements the Aztec diamond tiling algorithm described in [1] and [2].

Run 'interface.py' to draw random tiling on screen (requires pygame).

Classes
- Partition(parts):
    takes as input a non-increasing list of integers
    
    methods:
    
      - get(i) : returns the i-th part
      
      - set(i, x) : set the i-th part to x if the result is a valid partition

Functions
- interlace(p1, p2): 
    returns True if partitions p1 and p2 are interlaced
    
- dual_interlace(p1, p2): 
    returns True if partitions p1 and p2 are dual interlaced

- diagonal(d, lam, i):
    helper function for configuration(L)
    returns the Maya diagram of partition lam such that the number of particles
    above the i-th diagonal element is equal to the number of holes below the 
    i-th diagonal element
    
- configuration(L): 
    takes a list of partitions L of length 2n+1 and returns the Maya diagram of L
    refer to the code for the format of Maya diagram
    
- random_partitions(n, weights): 
    returns a random sequence of partitions of length 2n+1 that satisfies the 
    interlacing condition, based on the given weights
    

[1] 'From Aztec diamonds to pyramids: steep tilings' (2017), J. Bouttier, G. Chapuy, S. Corteel 

[2] 'Perfect sampling algorithms for Schur processes' (2018), D. Betea, C. Boutillier, J. Bouttier, G. Chapuy, S. Corteel, M. Vuletic

For more information, feel free to contact me at
NICOLAS RUAN 
nicolasruan@hotmail.com
