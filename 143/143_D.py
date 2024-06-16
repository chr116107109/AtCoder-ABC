

N = int(input())
A = list(map(int,input().split()))

ans = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i] < A[j] + A[k]:
                if A[j] < A[i] + A[k]:
                    if A[k] < A[j] + A[i]:
                        ans += 1

print(ans)