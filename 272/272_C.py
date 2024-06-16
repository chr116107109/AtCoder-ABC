
N = int(input())
A = list(map(int,input().split()))

kisu = []
gusu = []
for i in range(N):
    if A[i]%2 == 0:
        gusu.append(A[i])
    else:
        kisu.append(A[i])

if len(kisu) == 1 and len(gusu) == 1:
    print(-1)
else:
    gusu.sort()
    kisu.sort()
    
    if len(gusu) <= 1:
        ans = kisu[-1] + kisu[-2]
    elif len(kisu) <= 1:
        ans = gusu[-1] + gusu[-2]
    else:
        ans = max(gusu[-1] + gusu[-2],kisu[-1] + kisu[-2])
    print(ans)