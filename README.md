# aztec-diamond-tilings
Random tilings of Aztec Diamond

The partitions library implements some commonly used notions regarding partitions:

Classes
- Partition(parts):
    takes as input a non-increasing list of integers and returns the Partition object
    methods:
      - get(i) : returns the i-th part
      - set(i, x) : tries to set the i-th part to x

Functions
- interlace(p1, p2): 
    check if p1 > p2
- dual_interlace(p1, p2): 
    check if p1 >' p2 (equivalently p1'> p2' where ' is conjugation)
- configuration(L): 
    takes a list of partitions L of length 2n+1 and returns the Maya diagram of L
- random_partitions(n, weights): 
    returns a random sequence of partitions of length 2n+1 that satisfies the 
    interlacing condition, based on the given weights

The interface script provides a user friendly interface for generating random partitions and drawing the corresponding tiling using the pygame library. 


Nicolas Ruan
