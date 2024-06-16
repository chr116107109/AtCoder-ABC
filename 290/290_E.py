
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
A = list(map(int,input().split()))

before = Counter()
after = Counter()
sum_after = 0
ans = 0

if N%2 == 0:
    m = N//2
else:
    m = N//2

for i in range(N):
    before[A[i]] += 1

if N%2 == 0:
    for i in range(N):

        if i >= m:
            after[A[i]] -= N-i
            sum_after -= N-i

        before[A[i]] -= 1
        ans += (max(N-2*i-1,0) - max(before[A[i]],0))*(i+1)
        ans += sum_after - after[A[i]]

        if i < m:
            before[A[N-i-1]] -= 1
            after[A[N-i-1]] += i+1
            sum_after += i+1
        
else:        
    for i in range(N):

        if i > m:
            after[A[i]] -= N-i
            sum_after -= N-i

        before[A[i]] -= 1
        ans += (max(N-2*i-1,0) - max(before[A[i]],0))*(i+1)
        ans += sum_after - after[A[i]]

        if i < m:
            before[A[N-i-1]] -= 1
            after[A[N-i-1]] += i+1
            sum_after += i+1




print(ans)
