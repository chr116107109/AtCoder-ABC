
import itertools

N,W = map(int,input().split())
A = list(map(int,input().split()))
A.append(0)
A.append(0)

D = set()

for a,b,c in itertools.combinations(A,3):
    if (not a+b+c in D) and a+b+c <= W:
        D.add(a+b+c)


print(len(D))
