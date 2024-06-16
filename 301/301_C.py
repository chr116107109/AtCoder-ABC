
S = input()
T = input()
N = len(S)

from collections import Counter
cs = Counter()
ts = Counter()
for i in range(N):
    cs[S[i]] += 1
    ts[T[i]] += 1

x = 0
for i in ts:
    if i == '@':
        continue
    if ts[i] != cs[i] and (not i in 'atcoder'):
        x += 10**6
    x += max(ts[i] - cs[i],0)

y = 0
for i in cs:
    if i == '@':
        continue
    if ts[i] != cs[i] and (not i in 'atcoder'):
        y += 10**6
    y += max(cs[i] - ts[i],0)


if x <= cs['@'] and y <= ts['@']:
    print('Yes')
else:
    print('No')