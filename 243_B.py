
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

X = 0
Y = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                X += 1
            else:
                Y += 1

print(X)
print(Y)
