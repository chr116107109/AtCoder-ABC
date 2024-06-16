

N = int(input())
A = list(map(int,input().split()))

d = [0] * (N)
p = [0] * (N)
p[0] = 1
p[1] = -1
mod=998244353

for i in range(N-1):
    '''
    for j in range(1,A[i]+1):
        if i+j <= N:
            a = A[i]+1
            p[i+j] += p[i]*pow(a-1,mod-2,mod)
            p[i+j] %= mod

    '''
    if i > 0:
        p[i] += p[i-1]
    p[i] %= mod
    p[i+1] += p[i]*pow(A[i],mod-2,mod)
    p[i+1] %= mod
    if i+A[i]+1 < N:
        p[i+A[i]+1] -= p[i]*pow(A[i],mod-2,mod)
        p[i+A[i]+1] %= mod
    
    #print(p)
p[-1] += p[-2]
p[-1] %= mod
dd = [0] * N
for i in range(N-1):
    '''
    d[i] *= pow(p[i],mod-2,mod)
    d[i] %= mod
    for j in range(1,A[i]+1):
        if i+j <= N:
            a = A[i]+1
            d[i+j] += (d[i]*a+a-d[i])*pow(a-1,mod-2,mod)*pow(a-1,mod-2,mod)*p[i]
            d[i+j] %= mod
    '''
    a = A[i]+1
    dd[i] += dd[i-1]
    dd[i] %= mod
    d[i] += dd[i]
    d[i] *= pow(p[i],mod-2,mod)
    d[i] %= mod
    dd[i+1] += (d[i]*a+a-d[i])*pow(a-1,mod-2,mod)*pow(a-1,mod-2,mod)*p[i]
    dd[i+1] %= mod    
    if i+A[i]+1 < N:
        dd[i+A[i]+1] -= (d[i]*a+a-d[i])*pow(a-1,mod-2,mod)*pow(a-1,mod-2,mod)*p[i]
        dd[i+A[i]+1] %= mod
    #'''
    #print(d)
    #print(dd)

dd[-1] += dd[-2]
dd[-1] %= mod
d[-1] += dd[-1]
d[-1] *= p[-1]
d[-1] %= mod

print(d[-1])