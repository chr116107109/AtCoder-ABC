

N = int(input())
A = list(map(int,input().split()))


class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

mod = 998244353

B = [[i,A[i]] for i in range(N)]
B.sort(key=lambda x: (10**10)*x[1]+x[0])
ind2rank = [0] * N
q = Bit(N)
for i in range(N):
    ind2rank[B[i][0]] = i+1
    if B[i][0] > 0:
        q.add(i+1,pow(2,B[i][0]-1,mod))

import sys
#sys.exit()
ans = 0
import bisect
for i in range(N):
    #print([q.sum(j)-q.sum(j-1) for j in range(1,N+1)])

    k = ind2rank[i]-1
    a = q.sum(N)
    a -= (q.sum(k+1))
    #print(a,pow(2,(i*(mod-2))%(mod-1),mod), q.sum(k))
    #a //= pow(2,i,mod)
    a *= pow(2,(i*(mod-2))%(mod-1),mod)
    ans += a%mod
    ans %= mod
    
    #print(ans,a,k,'ans')

    if i > 0:
        q.add(ind2rank[i],-pow(2,i-1,mod))
    
print(ans)