
N = int(input())
A = list(map(int,input().split()))

B = []
ans = 0
for i in range(N):
    if A[i] == i+1:
        B.append(i)
    elif A[i] > i+1 and A[A[i]-1] == i+1:
        ans += 1

if B:
    ans += len(B)*(len(B)-1)//2

print(ans)