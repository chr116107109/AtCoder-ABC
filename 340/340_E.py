import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def debug(self):
        a = []
        print("tree",self.tree)
        for i in range(self.size+1):
            a.append(self.sum(i))
        print("ruiseki",a)
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

bit = Bit(N)    

bit.add(1,A[0])
for i in range(1,N):
    bit.add(i+1,A[i]-A[i-1])

#bit.debug()
for i in range(M):
    ind = B[i]

    x = bit.sum(ind+1)
    bit.add(1, x//N)
    bit.add(ind+1, -x)
    bit.add(ind+2, +x)
    bit.add(ind+2, 1)

    if ind + x%N + 2 <= N:
        bit.add(ind + x%N + 2, -1)
    else:
        bit.add(1, 1)
        bit.add(ind + x%N - N + 2, -1)
    
    #bit.debug()
        
print(*[bit.sum(i+1) for i in range(N)])
