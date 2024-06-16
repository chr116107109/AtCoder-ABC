from collections import Counter
H,W = map(int,input().split())
S = [input() for i in range(H)]
SS = Counter()
for x in zip(*S):
    SS[x] += 1
T = [input() for i in range(H)]
TT = Counter()
for x in zip(*T):
    TT[x] += 1

ans = 'Yes'
for s in SS:
    if SS[s] == TT[s]:
        continue
    else:
        ans = 'No'
        break

print(ans)