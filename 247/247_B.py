
from collections import Counter

N = int(input())
S,T = [],[]
d = Counter()
for i in range(N):
    s,t = input().split()
    S.append(s)
    T.append(t)
    d[s] += 1
    d[t] += 1
ans = 'Yes'
for i in range(N):
    if d[S[i]] > 1 and d[T[i]] > 1 and S[i] != T[i]:
        ans = 'No'
        break
print(ans)