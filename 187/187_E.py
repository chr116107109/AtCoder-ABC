
N = int(input())
g = [[] for i in range(N)]
E = []
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)
    E.append([a-1,b-1])

from collections import deque
class EularTour():

    def __init__(self, g):
        self.N = len(g)
        self._in = [0]*N
        self._out = [0]*N
        self.visited = []
        self.depth = [0] * N
        self._dfs()

    def _dfs(self):
        v = set()
        q = deque()
        q.append([0,0])
        while q:
            s,d = q.pop()
            if self.visited == [] or self.visited[-1] != s:
                self.visited.append(s)
            
            if s in v:
                self._out[s] = len(self.visited)-1
                continue
            else:
                self._in[s] = len(self.visited)-1
                q.append([s,d])
                self.depth[s] = d
                v.add(s)
            for t in g[s]:
                if t in v:
                    continue
                q.append([t,d+1])
            

ET = EularTour(g)

A = [0] * (len(ET.visited)+1)
Q = int(input())
for i in range(Q):
    t,e,x = map(int,input().split())
    a,b = E[e-1][(t+1)%2], E[e-1][t%2]

    if ET.depth[a] < ET.depth[b]:
        A[0] += x
        A[ET._in[b]] -= x
        A[ET._out[b]+1] += x
        A[len(ET.visited)] -= x
    else:
        A[ET._in[a]] += x
        A[ET._out[a]+1] -= x


B = [0] * len(ET.visited)
for i in range(1,len(ET.visited)):
    B[i] = B[i-1] + A[i-1]

ans = [0] * N
for i in range(len(ET.visited)-1):
    ans[ET.visited[i]] = B[i+1]

print(*ans,sep='\n')