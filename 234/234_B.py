
import itertools
import math

N = int(input())
X = [list(map(int,input().split())) for i in range(N)]

ans = 0
for u,v in itertools.combinations(X, 2):
    d = math.sqrt((u[0]-v[0])**2 + (u[1]-v[1])**2)
    ans = max(ans,d)


print(ans)
