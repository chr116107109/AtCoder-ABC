
N = int(input())
C = list(map(int,input().split()))

D = min(C)
M = N//D
N -= D*M

ans = []
for i in range(M):
    for j in range(8,-1,-1):
        if C[j] - D <= N:
            N -= C[j]-D
            break
    ans.append(str(j+1))

print(''.join(ans))