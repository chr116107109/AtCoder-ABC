import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = list(input())

Q = int(input())

reigai = {}
now = 0 # -1 small +1 big


for i in range(Q):

    q = list(input().split())

    if q[0] == '1':
        q[1] = int(q[1])
        if now != 0:
            reigai[q[1]-1] = q[2]
        S[q[1]-1] = q[2]
    if q[0] == '2':
        now = -1
        reigai = {}
    if q[0] == '3':
        now = 1
        reigai = {}


if now == -1:
    for i in range(N):
        if i in reigai:
            S[i] = reigai[i]
        else:
            S[i] = S[i].lower()
elif now == 1:
    for i in range(N):
        if i in reigai:
            S[i] = reigai[i]
        else:
            S[i] = S[i].upper()

print("".join(S))

