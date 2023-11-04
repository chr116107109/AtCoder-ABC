
N = int(input())
XY = [list(map(int,input().split())) for i in range(N)]


def build_graph(XY,S):
    g = [[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if abs(XY[i][0]-XY[j][0]) + abs(XY[i][1]-XY[j][1]) <= XY[i][2]*S:
                g[i].append(j)

    return g

from collections import deque
def bfs(start,g):
    visited = set()
    q = deque()
    q.append(start)
    count = 0
    while q:
        s = q.popleft()
        if s in visited:
            continue
        visited.add(s)
        count += 1
        if count == N:
            return True
        for t in g[s]:
            if not t in visited:
                q.append(t)

    return False


left = 1
right = 10**10

while left < right:
    m = (left + right)//2
    #print(left,right)
    g = build_graph(XY,m)
    #print(g)
    flag = 0
    for i in range(N):
        if bfs(i,g):
            flag = 1
            break
    
    if flag == 1:
        right = m
    else:
        left = m + 1

print(right)