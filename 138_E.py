import sys

S = input()
T = input()

d = {}
for i in range(len(S)):
    if S[i] in d:
        d[S[i]].append(i)
    else:
        d[S[i]] = [i]

for t in T:
    if not t in d:
        print(-1)
        sys.exit()

for s in d:
    d[s].sort()

import bisect

ans = 0
pos = -1
for t in T:
    ind = bisect.bisect_right(d[t], pos)
    if ind == len(d[t]):
        ans += len(S) - pos + d[t][0]
        pos = d[t][0]
    else:
        ans += d[t][ind] - pos
        pos = d[t][ind]

print(ans)
