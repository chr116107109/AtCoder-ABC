
A,B = map(int,input().split())

N = int(pow(A/B/2,2/3))

ans = 10**20
for n in [N-1,N,N+1]:
    if n < 0:
        continue
    ans = min(ans,N*B+A/pow(1+N,1/2))

print(ans)