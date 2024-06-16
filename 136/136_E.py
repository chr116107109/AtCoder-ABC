
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,K = map(int,input().split())

A = list(map(int,input().split()))

X = sum(A)
p = []
n = 2
while X > 1:
    if X%n == 0:
        p.append(n)
        X //= n
    n += 1
ans = 1
for i in p:
    m = 0
    for j in range(N):
        m += A[j]%i
    if m%i == 0 and m//2 <= K:
        ans = i

if sum(A)-max(A) <= K:
    ans = sum(A)
print(ans)
