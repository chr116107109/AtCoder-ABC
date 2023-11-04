
from audioop import mul
import itertools


N, k = map(int,input().split())
S = [input() for i in range(N)]

ans = 0

for i in range(2 ** N):
    bag = []
    for j in range(N): 
        if ((i >> j) & 1):
            bag.append(S[j])
    
    #print(bag)
    just_K = 0
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    num_alp = {s:0 for s in alphabets}
    for sent in bag:
        for s in alphabets:
            if s in sent:
                num_alp[s] += 1
    
    for s in num_alp:
        if num_alp[s] == k:
            just_K += 1
    
    ans = max(ans,just_K)
print(ans)