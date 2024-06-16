
N,K = map(int,input().split())
A = set(map(int,input().split()))

ans = -1
for i in range(K):
    if i in A:
        continue
    else:
        ans = i
        break

if ans >= 0:
    print(ans)
else:
    print(K)