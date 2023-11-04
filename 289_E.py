

T = int(input())

from collections import defaultdict, deque

def num(x,y):
    return 3000*x+y
def bfs(s,g_r,g_b):
    N = len(g_r)
    q = deque()
    q.append((s,0))
    visited = {}
    while q:
        s,d = q.popleft()
        sx,sy = s//3000, s%3000
        if s in visited:
            continue
        visited[s] = d
        if num(N-1, 0) in visited:
            break
        for tx in g_r[sx]:
            for ty in g_b[sy]:
                if num(tx,ty) in visited:
                    continue
                q.append((num(tx,ty),d+1))
        for tx in g_b[sx]:
            for ty in g_r[sy]:
                if num(tx,ty) in visited:
                    continue
                q.append((num(tx,ty),d+1))
    return visited


def solve():
    N,M = map(int,input().split())
    C = list(map(int,input().split()))
    g_r = [set() for i in range(N)]
    g_b = [set() for i in range(N)]
    for i in range(M):
        a,b = map(int,input().split())
        a,b = a-1,b-1

        if C[b] == 1:
            g_b[a].add(b) # kuro ni iku
        if C[b] == 0:
            g_r[a].add(b) # aka ni iku
        if C[a] == 1:
            g_b[b].add(a) # kuro ni iku
        if C[a] == 0:
            g_r[b].add(a) # aka ni iku

    visited = bfs(num(0,N-1),g_r,g_b)
    
    if num(N-1,0) in visited:
        return visited[num(N-1,0)]
    else:
        return -1
    
for i in range(T):
    print(solve())

