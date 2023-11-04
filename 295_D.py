


S = input()
N = len(S)
d = [0] * 10

from collections import Counter, defaultdict
C = defaultdict(list)
for i in range(N):
    n = int(S[i])
    d[n] += 1
    d[n] %= 2
    s = "".join(map(str,d))
    if s in C:
        C[s].append(i)
    else:
        C[s] = [i]

d = [0] * 10
ans = 0
import bisect
for c in C:
    if c == '0000000000':
        ans += len(C[c])
    if len(C[c]) > 1:
        n = len(C[c])
        ans += (n)*(n-1)//2

print(ans)
