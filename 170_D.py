
N = int(input())
A = list(map(int,input().split()))
A.sort()

ans = 0
B = set()
M = max(A)
for i in range(N):
    
    if (not A[i] in B) and A[i] != A[i-1] and A[i] != A[(i+1)%N]:
        ans += 1
    if A[i] == 1:
        break
    C = 0
    while C <= M:
        C += A[i]
        B.add(C)
    #print(B,ans)

if len(A) == 1:
    ans += 1
print(ans)