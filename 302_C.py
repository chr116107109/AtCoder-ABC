
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
import itertools

N,M = map(int,input().split())
S = [input() for i in range(N)]

ans = 'No'
for v in itertools.permutations(range(N)):

    is_ok = True
    for i in range(N-1):

        miss = 0
        for j in range(M):
            if S[v[i]][j] != S[v[i+1]][j]:
                miss += 1

        if miss != 1:
            is_ok = False
            break
    
    if is_ok:
        ans = 'Yes'
        break

print(ans)


