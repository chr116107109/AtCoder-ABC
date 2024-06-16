
N = int(input())
A = list(map(int,input().split()))

import random
from collections import deque
def bfs(s,g,visited):
    q = deque()
    q.append(s)
    while q:
        t = q.popleft()
        if t in visited:
            continue
        visited.add(t)
        for u in g[t]:
            q.append(u)
    return 

def main(N,A):
    #N = random.randint(1,20)
    #A = [random.randint(1,10) for i in range(N)]
    #print(N,A)
    g = [set() for i in range(max(A))]

    stats = set()
    for i in range(N//2):
        g[A[i]-1].add(A[N-i-1]-1)
        g[A[N-i-1]-1].add(A[i]-1)
        stats.add(A[N-i-1]-1)
        stats.add(A[i]-1)

    ans = len(stats)
    visited = set()

    for s in stats:
        if g[s] == set() or (s in visited):
            continue
        else:
            bfs(s,g,visited)
            ans -= 1
        #print(visited)

    print(ans)

main(N,A)