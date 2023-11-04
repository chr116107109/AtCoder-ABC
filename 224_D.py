from collections import defaultdict,deque
 
def num(A):
    res = 0
    for i in range(9):
        res += A[i]*10**i
    return res
d = {}
 
M = int(input())
g = [[] for i in range(9)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
p = list(map(int,input().split()))
for i in range(8):
    p[i] -= 1
p.append((set(range(9))-set(p)).pop()) 
# p: num to place

q = deque()
q.append((p,0))

from copy import deepcopy
while q:
    #print(q)
    p, dist = q.popleft()

    if num(p) in d:
        continue
    if p == [0,1,2,3,4,5,6,7,8]:
        d[num(p)] = dist
        break

    d[num(p)] = dist
    i = p[-1]
    indp = [0] * 9
    for k,n in enumerate(p):
        indp[n] = k
    for j in g[i]:
        k = indp[j]
        p_copy = [0]*9
        for i in range(9):
            p_copy[i] = p[i]
        p_copy[8], p_copy[k] = p_copy[k], p_copy[8] 
        q.append((p_copy, dist+1))


ans = [0,1,2,3,4,5,6,7,8]
if num(ans) in d:
    print(d[num(ans)])
else:
    print(-1)
