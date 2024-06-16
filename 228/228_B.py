
[N,X] = list(map(int,input().split()))
A = list(map(int,input().split()))

Y = A[X-1]

already = [X]
for i in range(N):
    already.append(Y)
    #print(Y)
    Y = A[Y-1]


print(len(set(already)))
