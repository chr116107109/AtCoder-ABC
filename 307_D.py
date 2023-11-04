import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
S = input()

q = deque()
count = 0
ans = []
for i in range(N):
    
    if S[i] == '(':
        count += 1
        q.append(S[i])
    elif S[i] == ')':
        if count > 0:
            while q:
                t = q.pop()
                if t == '(':
                    count -= 1
                    break
        else:
            q.append(')')
    else:
        q.append(S[i])

    #print(S)
print("".join(q))