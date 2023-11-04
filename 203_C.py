
N,K = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]
A.sort(key=lambda x:x[0])

i = 0
now = 0

for i in range(N):
    a,b = A[i]
    nec = a - now
    if K < nec:
        break
    K -= nec-b
    now = a

print(now+K)
