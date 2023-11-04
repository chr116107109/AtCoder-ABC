import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W = map(int,input().split())

A = [list(input()) for i in range(H)]


def strait(A,s,now,b):
    if s == '<':
        now[1] -= 1
    if s == '>':
        now[1] += 1
    if s == '^':
        now[0] -= 1
    if s == 'v':
        now[0] += 1

    a = {'<','>','v','^'}
    a.remove(s)
    while 0 <= now[0] < H and 0 <= now[1] < W and A[now[0]][now[1]] != '#':
        
        
        if s == '>' and A[i][j] == '<':
            A[now[0]][now[1]] = s+'!'
            break
        elif s == 'v' and A[i][j] == '^':
            A[now[0]][now[1]] = s+'!'
            break
        elif A[now[0]][now[1]] == s:
            break
        elif A[now[0]][now[1]] == '.':
            A[now[0]][now[1]] = s+'!'
        elif A[now[0]][now[1]] in a:
            break
    

        if s == '<':
            now[1] -= 1
        if s == '>':
            now[1] += 1
        if s == '^':
            now[0] -= 1
        if s == 'v':
            now[0] += 1


b = {'>!', '<!', 'v!', '^!'}

for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            S = [i,j]
        elif A[i][j] == 'G':
            G = [i,j]

for i in range(H):
    for j in range(W):
        if A[i][j] == 'S':
            continue
        elif A[i][j] == 'G':
            continue  
        elif A[i][j] == '#':
            continue
        elif A[i][j] == '.' or A[i][j] in b:
            continue
        else:
            strait(A,A[i][j],[i,j],b)
            #print(i,j)
            #print(*A,sep='\n')
            #print('')

from collections import deque
def bfs(s):
    q = deque()
    q.append((s,0))
    inf = 10**20
    visited = [[inf] * W for i in range(H)]
    while q:
        s,d = q.popleft()
        if visited[s[0]][s[1]] < inf:
            continue
        if A[s[0]][s[1]] != '.' and A[s[0]][s[1]] != 'S' and A[s[0]][s[1]] != 'G':
            continue 
        visited[s[0]][s[1]] = d
        for t in [[s[0]+1,s[1]],[s[0],s[1]+1],[s[0]-1,s[1]],[s[0],s[1]-1]]:
            if 0 <= t[0] < H and 0<= t[1] < W:
                q.append((t,d+1))
    return visited


visited = bfs(S)
if visited[G[0]][G[1]] == 10**20 or A[S[0]][S[1]] != 'S' or A[G[0]][G[1]] != 'G':
    print(-1)
else:
    print(visited[G[0]][G[1]])