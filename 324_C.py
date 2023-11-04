import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,T = input().split()
N = int(N)

ans = []
for i in range(N):
    S = input()
    if len(T) == len(S):
        miss = 0
        for j in range(len(T)):
            if S[j] != T[j]:
                miss += 1
        if miss <= 1:
            ans.append(i+1)
    elif abs(len(S)-len(T)) == 1 :
        mae = min(len(S),len(T))
        for j in range(min(len(S),len(T))):
            if S[j] != T[j]:
                mae = j
                break
        usiro = 0
        for j in range(min(len(S),len(T))):
            if S[-j-1] != T[-j-1]:
                usiro = max(len(S),len(T)) - j
                break
        if usiro - mae <= 1:
            ans.append(i+1)
        
        #print(S)
        #print(mae,usiro)

print(len(ans))
print(*ans)