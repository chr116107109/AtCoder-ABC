
S = input()

from collections import Counter
T = Counter()
for s in S:
    T[s] += 1

ans = -1
for s in S:
    if T[s] == 1:
        ans = s

print(ans)