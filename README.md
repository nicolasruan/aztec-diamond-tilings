# aztec-diamond-tilings
Random tilings of Aztec Diamond

Classes
- Partition(parts):
    takes as input a non-increasing list of integers and returns the Partition object
    methods:
      - get(i) : returns the i-th part
      - set(i, x) : set the i-th part to x if the result is a valid partition

Functions
- interlace(p1, p2): 
    return True if p1 > p2
- dual_interlace(p1, p2): 
    return True if p1 >' p2 
- configuration(L): 
    takes a list of partitions L of length 2n+1 and returns the Maya diagram of L
    refer to the code for the format of Maya diagram
- random_partitions(n, weights): 
    returns a random sequence of partitions of length 2n+1 that satisfies the 
    interlacing condition, based on the given weights

Run interface to draw random partition on screen (uses pygame library).

NR
