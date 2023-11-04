
N,Q = map(int,input().split())
A = []
for i in range(N):
    LA = list(map(int,input().split()))
    A.append(LA[1:])

for i in range(Q):
    s,t = map(int,input().split())
    print(A[s-1][t-1])