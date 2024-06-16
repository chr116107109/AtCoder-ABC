import math
import itertools

N = int(input())
X = [list(map(int,input().split())) for i in range(N)]

d = set()
for i,j in itertools.combinations(range(N),2):
    a,b = X[j][0] - X[i][0], X[j][1] - X[i][1]
    g = math.gcd(a,b)
    if not (a//g,b//g) in d:
        d.add((a//g,b//g))
    if not (-a//g,-b//g) in d:
        d.add((-a//g,-b//g))
    


print(len(d))