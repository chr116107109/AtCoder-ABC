
N,L,R = map(int,input().split())
A = list(map(int,input().split()))

g = []
for i in range(N):
    if A[i]%(L+R) < L:
        g.append(0)
    else:
        a = R//L
        b = R%L
        x = A[i]%(L+R)-L
        g.append(x//L+1)

ans = g[0]
if len(g) > 1:
    for v in g[1:]:
        ans ^= v

if ans == 0:
    print('Second')
else:
    print('First')