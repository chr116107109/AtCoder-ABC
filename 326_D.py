import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
R = input()
C = input()

def check(A):
    for i in range(N):
        a = Counter(A[i])
        if not (a['A'] == 1 and a['B'] == 1 and a['C'] == 1):
            return False
    for i in range(N):
        a = Counter([A[j][i] for j in range(N)])
        if not (a['A'] == 1 and a['B'] == 1 and a['C'] == 1):
            return False
    
    return True


for p in itertools.product(range(N),repeat=N):
    for q in itertools.product(range(N),repeat=N):
        A = [['.']*N for i in range(N)]
        for i in range(N):
            A[i][p[i]] = R[i]
        for i in range(N):
            A[q[i]][i] = C[i]
        
        if not check(A):
            continue

        print(A)