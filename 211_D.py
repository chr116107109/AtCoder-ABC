
N,M = map(int,input().split())
g = [[] for i in range(N)]
P = 10**9+7
for i in range(M):
    A,B = map(int,input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)


from collections import deque,Counter
q = deque()
q.append([0,0])
visited = {0:0} 
count = [0] * N
count[0] = 1
while q:
    [s,d] = q.popleft()
    for t in g[s]:
        if t in visited:
            if visited[s]+1 == visited[t]:
                count[t] += count[s]
                count[t] %=P
        else:
            visited[t] = d+1
            count[t] += count[s]
            q.append([t,d+1])


if N-1 in visited:
    print(count[N-1])
else:
    print(0)