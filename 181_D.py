from collections import Counter
import itertools
S = input()

C = Counter()
for s in S:
    C[s] += 1

N = 0
ans = 'No'
while N <= 1000:
    Ns = str(N)
    Ns = '0' * 3 + Ns
    Ns = Ns[-3:]
    D = Counter()
    for s in Ns:
        D[s] += 1
    flag = True
    for s in D:
        if D[s] > C[s]:
            flag = False
            break
    
    if flag:
        ans = 'Yes'
        break

    N += 8

if len(S) <= 3:
    for s in itertools.permutations(S):
        if int("".join(s)) % 8 == 0:
            ans = 'Yes'

print(ans)
    