
N,M,K = map(int,input().split())

P = 998244353

d = [[1]*M for i in range(N)]
sum_ = [i for i in range(M+1)]

for j in range(1,N):

    for i in range(M):
        
        if K > 0:
            d[j][i] = (sum_[max(i+1-K,0)]+ (sum_[M] - sum_[min(i+K,M)])) % P
        else:
            d[j][i] = sum_[M]


    for i in range(1,M+1):
        sum_[i] = (sum_[i-1] + d[j][i-1]) % P

    #print(d)
    #print(sum_)

print(sum_[M])