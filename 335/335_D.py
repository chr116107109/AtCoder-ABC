import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N = int(input())
E = []

def f(i,j):
    return i*N+j
def rf(k):
    return k//N,k%N

now = [N//2,N//2]
now[1] -= 1
ans = [[0]*N for i in range(N)]
ans[now[0]][now[1]+1] = 'T'
ans[now[0]][now[1]] = 1
count = 2
for i in range(N//2):
    for j in range(1+i*2):
        now[0] -= 1
        ans[now[0]][now[1]] = count
        count += 1
    for j in range(2*(i+1)):
        now[1] += 1
        ans[now[0]][now[1]] = count
        count += 1
    for j in range(2*(i+1)):
        now[0] += 1
        ans[now[0]][now[1]] = count
        count += 1
    for j in range(2*(i+1)):
        now[1] -= 1
        ans[now[0]][now[1]] = count
        count += 1
    
    #print(ans)
    if i == N//2-1:
        break
    now[1] -= 1
    ans[now[0]][now[1]] = count
    count += 1



for a in ans:
    print(*a)  