
N,T = map(int,input().split())
A = list(map(int,input().split()))
s = sum(A)

T %= s

for i in range(N):
    if T < A[i]:
        print(i+1,T)
        break
    else:
        T -= A[i]