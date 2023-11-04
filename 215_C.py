
S,K = input().split()
K = int(K)

import itertools

C = set()
for t in itertools.permutations(S):
    C.add(t)

C = sorted(list(C))
print("".join(C[K-1]))