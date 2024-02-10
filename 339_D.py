import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
import sys
N = int(input())
S = [input() for _ in range(N)]

a = []
b = []
for i in range(N):
    for j in range(N):
        if S[i][j] == 'P' and a == []:
            a = [i,j]
        elif S[i][j] == 'P':
            b = [i,j]


def f(i,j,a,b):
    return i + j*N + a*N**2 + b*N**3
def g(n):
    b = n//(N**3)
    n = n%(N**3)
    a = n//(N**2)
    n = n%(N**2)
    j = n//N
    i = n%N
    return [i,j,a,b]

def h(a,b):
    return a*(N**2)+b
def k(n):
    NN = N**2
    return [n//NN,n%NN]
from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    M = N**4+10
    visited = [-1] * M
    visited[s] = 0
    ans = 10**10
    while q:
        ori,d = q.popleft()
        i,j,a,b = g(ori)
        a_pos = [i,j]
        b_pos = [a,b]
        #print(a_pos,b_pos)
        #print(ori,visited[ori])
        if visited[ori] > 0:
            continue
        visited[ori] = d
        if a_pos == b_pos:
            ans = d
            break
        for t in [[0,1],[0,-1],[1,0],[-1,0]]:
            if 0 <= a_pos[0]+t[0] < N and 0 <= a_pos[1]+t[1] < N and S[a_pos[0]+t[0]][a_pos[1]+t[1]] != '#':
                a_next = [a_pos[0]+t[0],a_pos[1]+t[1]]
            else:
                a_next = a_pos
            if 0 <= b_pos[0]+t[0] < N and 0 <= b_pos[1]+t[1] < N and S[b_pos[0]+t[0]][b_pos[1]+t[1]] != '#':
                b_next = [b_pos[0]+t[0],b_pos[1]+t[1]]
            else:
                b_next = b_pos
            #print(a_pos,b_pos,a_next,b_next)
            ori = f(a_next[0],a_next[1],b_next[0],b_next[1])
            if visited[ori] == -1:
                q.append((ori,d+1))
    return ans

ans = bfs(f(a[0],a[1],b[0],b[1]))


if ans == 10**10:
    print(-1)
else:
    print(ans)