import sys
sys.setrecursionlimit(10 ** 6)  # 変更
from collections import Counter, deque

N = int(input())
A = list(map(int,input().split()))
g = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)


ans = set()
C = [0] * (10**5)
def dfs(s,C,par): 
    
    if C[A[s]-1] == 0:
        ans.add(s+1)
    for t in g[s]:
        if t == par:
            continue
        C[A[s]-1] += 1
        dfs(t,C,s)
        C[A[s]-1] -= 1
visited = set()
dfs(0,C,-1)
        
ans = sorted(list(ans))
for a in ans:
    print(a)