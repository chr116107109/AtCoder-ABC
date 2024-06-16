
A,B,N = map(int,input().split())

ans = 0
n = 1
k = 0
while n <= N and k <= A:
    k += 1
    ans = max(ans,(A*n)//B-A*(n//B))
    n = (B*k)//A
    if (B*k)%A > 0:
        n += 1
    #print(n,ans)

print(ans)