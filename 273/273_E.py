

A = []
d = {}
Q = int(input())

parent = [0] 
child = [-1]
g = [-1] 

now = 0
ans = []
for i in range(Q):
    q = input().split()

    if q[0] == 'ADD':
        g.append(q[1])
        parent.append(now)
        now = len(parent)-1
    if q[0] == 'DELETE':
        now = parent[now]
    if q[0] == 'SAVE':
        d[q[1]] = now
    if q[0] == 'LOAD':
        if q[1] in d:
            now = d[q[1]]
        else:
            now = 0


    ans.append(g[now])

print(*ans)