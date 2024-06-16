
N,Q = map(int,input().split())
g = {}

for i in range(Q):
    T,A,B = map(int,input().split())

    if T == 1:
        if A in g:
            g[A].add(B)
        else:
            g[A] = {B}
    if T == 2:
        if A in g:
            if B in g[A]:
                g[A].remove(B)
    if T == 3:
        if A in g and B in g:
            if B in g[A] and A in g[B]:
                print('Yes')
                continue
        
        print('No')