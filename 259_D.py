
def dist_squere(s,t):
    return ((s[0]-t[0])**2 + (s[1]-t[1])**2)

N = int(input())
sx,sy,tx,ty = map(int,input().split())
cir = [list(map(int,input().split())) for i in range(N)]

s = [sx,sy]
t = [tx,ty]
def make_g(cir):
    g = [[] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j and (cir[i][2]-cir[j][2])**2 <= dist_squere([cir[i][0],cir[i][1]],[cir[j][0],cir[j][1]]) <= (cir[i][2]+cir[j][2])**2:
                g[i].append(j)
    return g

def find_start_goal(cir,s,t):
    for i in range(N):
        if dist_squere([cir[i][0],cir[i][1]],s) == cir[i][2]**2:
            start = i
        if dist_squere([cir[i][0],cir[i][1]],t) == cir[i][2]**2:
            goal = i
    return start,goal

g = make_g(cir)
start,goal = find_start_goal(cir,s,t)

from collections import deque

d = deque()
d.append(start)

visited = set()
while d:
    now = d.popleft()
    if now in visited:
        continue
    visited.add(now)
    for next in g[now]:
        d.append(next)

if goal in visited:
    print('Yes')
else:
    print('No')