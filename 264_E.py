import sys
sys.setrecursionlimit(10**8)

def find(d,x):
    if d[x][0] < 0:
        return x
    else:
        d[x][0] = find(d,d[x][0])
        return d[x][0]

def union(d,x,y):
    root_x = find(d,x)
    root_y = find(d,y)
    
    #d[root_x][1] = (d[root_x][1] or d[root_y][1])
    #d[root_y][1] = (d[root_x][1] or d[root_y][1])

    if root_x == root_y:
        return 

    d[root_x][0] += d[root_y][0]
    d[root_y][0] = root_x
    #if d[root_x][0] <= d[root_y][0]:
        #d[root_x][0] += d[root_y][0]
        #d[root_y][0] = root_x
    #elif d[root_x][0] > d[root_y][0]:
        #d[root_y][0] += d[root_x][0]
        #d[root_x][0] = root_y

N,M,E = map(int,input().split())
UV = [list(map(int,input().split())) for i in range(E)]
Q = int(input())
X = [int(input()) for i in range(Q)]

X_set = set(X)
d = [[-1,False] for i in range(N)] + [[-1,True]]
for i in range(E):
    if i+1 in X_set:
        continue
    else:
        [u,v] = [UV[i][0]-1,UV[i][1]-1]
        u,v = min(u,N),min(v,N)
        union(d,u,v)


ans = [-d[find(d,N)][0] - 1]
X.reverse()
for i in range(Q):
    [u,v] = [UV[X[i]-1][0]-1,UV[X[i]-1][1]-1]
    u,v = min(u,N),min(v,N)
    #print(u,v)
    u = find(d,u)
    v = find(d,v)
    #print(u,v)
    
    union(d,u,v)
    ans.append(-d[find(d,N)][0] - 1)

ans = ans[:-1]
ans.reverse()
for i in range(Q):
    print(ans[i])

