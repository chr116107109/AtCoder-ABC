
from collections import Counter

def calc(s,t):
    cs = Counter(s)
    ct = Counter(t)
    score_s = 0
    for i in range(1,10):
        i = str(i)
        if i == '#':
            continue
        score_s += int(i)*pow(10,cs[i])
    score_t = 0
    for i in range(1,10):
        i = str(i)
        if i == '#':
            continue
        score_t += int(i)*pow(10,ct[i])
    
    return score_s > score_t
    
K = int(input())
S = input()
T = input()

card = {str(i):K for i in range(1,10)}
for i in range(4):
    card[S[i]] -= 1
    card[T[i]] -= 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        if i!=j:
            if calc(S[:-1]+str(i),T[:-1]+str(j)):
                ans += card[str(i)]*card[str(j)]
        if i==j:
            if calc(S[:-1]+str(i),T[:-1]+str(j)):
                ans += card[str(i)]*max(card[str(j)]-1,0)

import math
#print(ans)
ans /= sum(card.values())*(sum(card.values())-1)
print(ans)
