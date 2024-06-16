
from collections import Counter
N = int(input())
S = Counter()
for i in range(N):
    s = input()
    if S[s] > 0:
        print(s+'({})'.format(S[s]))
    else:
        print(s)

    S[s] += 1