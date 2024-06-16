
def comb(N,A,mod):
    res = 1
    if N < A:
        return 0
    for i in range(A):
        res *= N
        res %= mod
        N -= 1
    for i in range(A):
        res *= pow(A,mod-2,mod)
        res %= mod
        A -= 1

    return res


N,A,B = map(int,input().split())
mod = 10**9 + 7
ans = pow(2,N,mod) - comb(N,A,mod) - comb(N,B,mod) - 1 
ans %= mod
print(ans)