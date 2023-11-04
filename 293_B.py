
N = int(input())
A = list(map(int,input().split()))

ans = set(range(1,N+1))

for i in range(1,N+1):
    if A[i-1] in ans and i in ans:
        ans.remove(A[i-1])

ans = sorted(list(ans))
print(len(ans))
print(*ans)