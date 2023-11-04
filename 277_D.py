
from collections import Counter
N,M = map(int,input().split())
A = list(map(int,input().split()))

C = Counter()
for i in range(N):
    C[A[i]] += 1

B = sorted(list(C.keys()))
D = [[B[0]]]
now = 0
for i in range(len(B)-1):
    if (B[i]+1)%M == B[i+1]:
        D[now].append(B[i+1])
    else:
        D.append([B[i+1]])
        now += 1

if len(D) > 1 and (B[-1]+1)%M ==B[0]:
    D[0] += D.pop()

t = 0
for d in D:
    s = sum([b*C[b] for b in d])
    t = max(t,s)

ans = sum([b*C[b] for b in C]) - t
print(ans)