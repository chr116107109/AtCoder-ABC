
H,W = map(int,input().split())
A = [input() for i in range(H)] 


g = [[] for i in range(26)]
def num(a):
    return ord(a)-97
for i in range(H):
    for j in range(W):
        if 'a' <= A[i][j] <= 'z':
            g[num(A[i][j])].append([i,j])
        if A[i][j] == 'S':
            S = (i,j)
        if A[i][j] == 'G':
            G = (i,j)

from collections import deque

q = deque()
q.append([S[0],S[1],0])
inf = 10**10
visited = [[inf]*W for i in range(H)]
vis = set()
ans = -1
count = 0
while q:
    #count += 1
    #print(q)
    i,j,d = q.popleft()
    if visited[i][j] < inf:
        continue
    if (i,j) == G:
        ans = d
        break
    visited[i][j] = d

    if 'a'<=A[i][j]<='z':
        if not A[i][j] in vis:
            for t in g[num(A[i][j])]:
                if [i,j] != t:
                    if visited[t[0]][t[1]] < inf:
                        continue
                    visited[i][j] = d+1
                    q.append([t[0],t[1],d+1])
            vis.add(A[i][j])
        
    for dif in [[1,0],[0,1],[-1,0],[0,-1]]:
        t = [i+dif[0],j+dif[1]]
        if 0<=t[0]<H and 0<=t[1]<W and A[t[0]][t[1]] != '#':
            if visited[t[0]][t[1]] < inf:
                continue
            visited[i][j] = d+1
            q.append([t[0],t[1],d+1])
    
print(ans)