
N,P,Q,R,S = map(int,input().split())
A = list(map(int,input().split()))

for i in range(Q-P+1):
    A[P+i-1],A[R+i-1] = A[R+i-1],A[P+i-1]

print(*A)