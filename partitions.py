import numpy as np


class Partition:
    def __init__(self, parts):
        # parts : decreasing list of positive non-zero integers
        self.parts = parts
        self.length = len(parts)

    def get(self, i): 
        if i == 0: return 10**10 # by convention part zero is +infinity
        if i<=self.length:
            return self.parts[i-1]
        else:
            return 0

        self.length = len(self.parts)

    def set(self, i, x):
        if x==0: return
        
        if 0 < i <= self.length:
            self.parts[i-1] = x
        elif i == self.length+1:
            self.parts.append(x)

        self.length = len(self.parts)

    def display(self):
        print("partition" + self.parts)
        for part in self.parts:
            print(part*"*")

    
def dual_cauchy(l, m, k, B):
    # input: l >' k < m partitions, B in {0, 1}
    # output: partition n with l < n >' m
    L = max(l.length, m.length)
    n = Partition( list() )
    for i in range(1, L+2):
        mi = m.get(i)
        li = l.get(i)
        ki = k.get(i)
        if li <= mi < l.get(i-1):
            n.set(i, max(li, mi) + B)
        else:
            n.set(i, max(li, mi))
        if m.get(i+1) < li <= mi:
            B = min(li, mi) - ki
    return n

#la = Partition([2, 2, 1, 1])
#mu = Partition([4, 1])
#ka = Partition([1, 1])
#B = 0

def interlace(p1, p2):
    # input: p1, p2 partitions
    # output:   True if p1 > p2
    #           False otherwise
    L = max(len(p1.parts), len(p2.parts))
    interlace = True
    for k in range(1, L+1):
        if p1.get(k) < p2.get(k) or p1.get(k+1) > p2.get(k):
            interlace = False
    return interlace

def dual_interlace(p1, p2):
    # input: p1, p2 partitions
    # output:   True if p1 >' p2
    #           False otherwise
    L = max(len(p1.parts), len(p2.parts))
    dual_interlace = True
    for k in range(1, L+1):
        D = p1.get(k) - p2.get(k)
        if D<0 or D>1 :
            dual_interlace = False
    return dual_interlace
    

def diagonal(d, lam, i):
    # input:    list d of zeros (n if i even, n+1 if i odd)
    #           partition lam
    #           integer i (diagonal index 0, 1, ..., 2n)
    # output:   maya diagram of lam such that the
    #           number of particles (1) above i
    #           is equal to the number of holes (0)
    #           under i
    length = len(d)
    n = len(lam.parts)
    parts = [ lam.parts[n-k] for k in range(1, n+1) ]
    for part in parts:
        if part != 0:
            count = 0
            j = 0
            while count < part:
                if d[j] == 0:
                    count+=1
                j+=1
            while d[j] != 0:
                j += 1
            d[j] = 1

    mid = (i + (i%2))/2 # index of line y = 0
    holes = 0 # below y=0
    particles = 0 # above y=0
    for k in range(0, len(d)):
        if k< mid:
            if d[k] == 0:
                holes +=1
        if k >= mid:
            if d[k] == 1:
                particles += 1
    diff = abs(holes-particles)
    for k in range(0, diff):
        d.insert(0, 1)
    d = d[0:length]
        
            
    return d


def configuration(L):
    #input:     L = [l_0, l_1, ..., l_2n] list of partitions
    #output:    particle configuration C = [d_0, d_1, ..., d_2n]
    #           where d_i is the maya diagram of l_i for all i
    n = int((len(L)-1)/2)
    PC = []
    for k in range(0, len(L)):
        C = [0 for i in range(0, n)]
        if k%2 == 1:
            C.append(0)

        C = diagonal(C, L[k], k)
        PC.append(C)
    return PC


def random_partitions(n, weights):
    #input:     n order of the aztec diamond
    #           weights list of n*(n+1)/2 real numbers in [0, 1]
    #output:    list of 2*n+1 partitions that
    #           satisfies the interlacing condition 
    B = int(n*(n+1)/2)
    c = np.random.rand(B)
    b = []
    for k in range(0, len(c)):
        if c[k] > weights[k]:
            b.append(0)
        else:
            b.append(1)
    k = 0
    L = [ [Partition([]) for i in range(0, j)] for j in range(1, n+3) ]
    for i in range(0, n+2):
        L[i][0] = Partition([0])
        L[i][i] = Partition([0])
    for i in range(1, n+2):
        for j in range(1, i):
            la = L[i-1][j-1]
            mu = L[i-1][j]
            ka = L[i-2][j-1]
            L[i][j] = dual_cauchy(la, mu, ka, b[k])
            k+=1


    partitions = []
    for i in range(0, 2*n+1):
        if i%2==0:
            k = n
        else:
            k = n+1
        x = int((i + (i%2))/2)
        partitions.append(L[k][x])

    return partitions


