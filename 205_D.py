import bisect
N,Q = map(int,input().split())
A = list(map(int,input().split()))
B = [0] * (N)
B[0] = A[0]-1
for i in range(1,N):
    B[i] = B[i-1] + (A[i]-A[i-1]-1)
for i in range(Q):
    K = int(input())
    ind = bisect.bisect_left(B,K)
    if ind == 0:
        print(K)
    elif ind == N:
        print(A[-1]+K-B[-1])
    else:
        print(A[ind-1] + (K-B[ind-1]))