
N = int(input())
A = list(map(int,input().split()))

now = A[0]
ans = [A[0]]
for i in range(1,N):
    if A[i] > now+1:    
        for j in range(now+1,A[i]):
            ans.append(j)
    if A[i] < now-1:
        for j in range(now-1,A[i],-1):
            ans.append(j)
    ans.append(A[i])
    now = A[i]
print(*ans)