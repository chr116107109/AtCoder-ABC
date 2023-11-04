
N,X,Y,Z = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

C = [[A[i],B[i],i+1] for i in range(N)]

ans = []
C.sort(key=lambda x:x[0]*(N+1) - x[2])
for i in range(X):
    D = C.pop()
    ans.append(D[-1])
C.sort(key=lambda x:x[1]*(N+1) - x[2])
for i in range(Y):
    D = C.pop()
    ans.append(D[-1])
C.sort(key=lambda x:(x[1]+x[0])*(N+1) - x[2])
for i in range(Z):
    D = C.pop()
    ans.append(D[-1])

ans.sort()
for a in ans:
    print(a)