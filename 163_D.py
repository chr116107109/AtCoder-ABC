
N,K = map(int,input().split())

def sum_arr(s,g):
    return ((s+g)*(g-s+1))//2


ans = 0
for i in range(K,N+1):
    ans += sum_arr(N-i+1,N) -  sum_arr(0,i-1) + 1
    ans %= 10**9+7
    #print(ans)

print((ans+1)%(10**9+7))
