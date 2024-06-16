
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools



N = int(input())
S = input()
T = input()

ans = 'Yes'
for i in range(N):
    x,y = S[i],T[i]
    x,y = min(x,y),max(x,y)
    if x == y or (x == '1' and y == 'l') or (x=='0' and y=='o'):
        continue
    else:
        ans = 'No'
        break

print(ans)
