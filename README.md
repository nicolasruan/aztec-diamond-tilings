# aztec-diamond-tilings
Random tilings of Aztec Diamond

The partitions library features some commonly used functions for working with partitions:
interlace(p1, p2): check if p1 > p2
dual_interlace(p1, p2): check if p1 >' p2 (equivalently p1'> p2' where ' is conjugation)
configuration(L): takes a list of partitions L of length 2*n + 1 and returns the Maya diagram of L
random_partitions(n): returns a random sequence of partitions of length 2*n+1 that satisfies the 
interlacing condition

TO DO: weighted model

The interface script visualizes domino tilings. It depends on the pygame library for graphics.
