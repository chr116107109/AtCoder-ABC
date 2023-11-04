
N,X,Y = map(int,input().split())
X,Y = min(X-1,Y-1),max(X-1,Y-1)

import itertools

dict = [0] * (N-1)
for i,j in itertools.combinations(range(N),2):
    i,j = min(i,j),max(i,j)
    
    d = min(j-i, abs(X-i) + 1 +abs(Y-j))
    dict[d-1] += 1

for d in dict:
    print(d)