
N,H = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]

M = 10**9
A.sort(key=lambda x: x[0]*M-x[1])

a = A.pop()

A.sort(key=lambda x: -x[1])
ans = 0
import sys
if A:
    for i in range(N-1):
        if A[i][1] > a[0]:
            ans += 1
            H -= A[i][1]
        
        if H <= 0:
            print(ans)
            sys.exit()

H -= a[1]
ans += 1
H = max(0,H)
ans += -(-H//a[0])
print(ans)



