

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A,B = map(int,input().split())
S = input()

ans = 'Yes'
for i in range(A):
    if not '0' <= S[i] <= '9':
        ans = 'No'

if not S[A] == '-':
    ans = 'No'

for i in range(A+1,A+B+1):
    if not '0' <= S[i] <= '9':
        ans = 'No'

print(ans)