
N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

ans = 0

now = 1
B = []
if A:
    if A[0] > 1:
        B.append(A[0]-1)
    if A[-1] < N:
        B.append(N-A[-1])

    for i in range(M-1):
        if A[i+1] - A[i] > 1:
            B.append(A[i+1] - A[i]-1)

    if B == []:
        ans = 0
    else:
        K = min(B)
        ans = sum([-(-b//K) for b in B])
    print(ans)
else:
    print(1)