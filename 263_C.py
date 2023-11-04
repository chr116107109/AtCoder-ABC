
import itertools


N,M = map(int,input().split())
A = []
for a in itertools.combinations(range(1,M+1),N):
    ans = list(a)
    ans.sort()
    A.append(ans)

#A.sort(key = lambda x:int(''.join(list(map(str,x)))))
A.sort()
for a in A:
    print(*a)