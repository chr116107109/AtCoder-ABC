

N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = set(map(int,input().split()))
X = int(input())

d = [0] * (X+1)
d[0] = 1
for i in range(X+1):
    if d[i] == 1:
        for j in range(N):
            if i + A[j] in B or i + A[j] > X:
                continue
            d[i+A[j]] = 1

if d[X] == 1:
    print('Yes')
else:
    print('No')