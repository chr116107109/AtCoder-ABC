
H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
H1, W1 = map(int, input().split())
B = [list(map(int, input().split())) for i in range(H1)]

import itertools
ans = 'No'
for p in itertools.combinations(range(H),H1):
    C = []
    p = sorted(list(p))
    for i in p:
        C.append(A[i])
    C = list(map(list, zip(*C)))
    for q in itertools.combinations(range(W),W1):
        D = []
        q = sorted(list(q))
        for i in q:
            D.append(C[i])
        D = list(map(list, zip(*D)))
        #print(D)
        if D == B:
            ans = 'Yes'
            break

print(ans)