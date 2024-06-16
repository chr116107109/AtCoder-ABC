
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

left = [0]
right = [0]
for i in range(N-1,0,-1):
    right.append(math.gcd(right[-1],A[i]))

ans = 0
for i in range(N):
    #print(left)
    #print(right)
    ans = max(ans,math.gcd(left[-1],right[-1]))
    left.append(math.gcd(left[-1],A[i]))
    right.pop()

print(ans)