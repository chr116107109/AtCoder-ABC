
N = int(input())
A = list(map(int,input().split()))
import itertools
ans = 10**20
for i in range(N):
    for k in itertools.combinations(range(1,N),i):
        k = sorted(list(k))
        k.append(N)
        a = 0
        now = 0
        #print(k)
        for j in k:
            sub = 0
            for aa in A[now:j]:
                sub |= aa
            now = j
            a ^= sub
        #print(a)
        ans = min(ans,a)

print(ans)