
N = int(input())
A = list(map(int,input().split()))

P = 0
rui = [0] * 4
for i in range(N):
    rui[0] = 1
    for j in range(3,-1,-1):
        if rui[j] == 1:
            if j+A[i] > 3:
                P += 1
                rui[j] = 0
            else:
                rui[j],rui[j+A[i]] = 0,1

print(P)
    