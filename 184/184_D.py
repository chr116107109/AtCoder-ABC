
A,B,C = map(int,input().split())

from collections import deque
q = deque()
d = [[[0] * 101 for i in range(101)] for i in range(101)]

q.append((A,B,C))
ans = 0
visited = set()
d[A][B][C] = 1
while q:
    s = q.popleft()
    a,b,c = s
    v = d[a][b][c]
    if s in visited:
        continue
    visited.add((a,b,c))
    #print(s)
    #print(d[s[0]][s[1]][s[2]])
    if 100 in s:
        ans += (sum(s)-(A+B+C))*d[s[0]][s[1]][s[2]]
        #print(ans)
        continue
    
    if a>0:
        q.append((a+1,b,c))
        d[a+1][b][c] += a*(v)/(a+b+c)
    if b>0:
        q.append((a,b+1,c))
        d[a][b+1][c] += b*(v)/(a+b+c)
    if c>0:
        q.append((a,b,c+1))
        d[a][b][c+1] += c*(v)/(a+b+c)

print(ans)