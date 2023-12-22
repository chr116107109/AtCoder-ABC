import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
from sys import exit

N = int(input())

enemy = Counter()
portion = defaultdict(list)

A = []
counter = 0
ind2ind= {}
for i in range(N):
    t,x = map(int,input().split())
    if t == 1:
        ind2ind[counter] = i
        portion[x].append(counter)
        counter += 1
    A.append((t,x))

for p in portion:
    portion[p].sort()

ans = [0] * counter

ans_count = 0
Count = 0
plan_to_use = set()
for i in range(N-1,-1,-1):
    t,x = A[i]
    #print(portion)
    
    if t == 2:
        if len(portion[x]) == 0:
            print('-1')
            exit()
        else:
            ind = portion[x].pop()
            ans[ind] = 1
            Count += 1
            plan_to_use.add(ind2ind[ind])
    else:
        if i in plan_to_use:
            Count -= 1
            plan_to_use.remove(i)
        else:
            portion[x].pop()

    ans_count = max(ans_count,Count)
    #print(plan_to_use)

print(ans_count)
print(*ans)
