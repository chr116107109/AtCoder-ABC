import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N,X,Y = map(int,input().split())

A = list(map(int,input().split()))

tate = [A[i] for i in range(N) if i%2 == 0]
yoko = [A[i] for i in range(N) if i%2 == 1]

def get_kouho(A):
    res = {}
    for bit in range(2**len(A)):
        score = 0
        s = ''
        for i in range(len(A)):
            if bit & (1<<i) == 0:
                score -= A[i]
                s += 'N'
            else:
                score += A[i]
                s += 'P'
        res[score] = s

    return res

tate_kouho_0 = get_kouho(tate[:len(tate)//2])
tate_kouho_1 = get_kouho(tate[len(tate)//2:])

tate_bit = []
for t in tate_kouho_0:
    if Y-t in tate_kouho_1:
        tate_bit = [tate_kouho_0[t], tate_kouho_1[Y-t]]
yoko_kouho_0 = get_kouho(yoko[:len(yoko)//2])
yoko_kouho_1 = get_kouho(yoko[len(yoko)//2:])

yoko_bit = []
for y in yoko_kouho_0:
    if X-y in yoko_kouho_1:
        yoko_bit = [yoko_kouho_0[y], yoko_kouho_1[X-y]]


if tate_bit == [] or yoko_bit == []:
    print("No")
    sys.exit()

tate_bit = tate_bit[0] + tate_bit[1]
yoko_bit = yoko_bit[0] + yoko_bit[1]
merged_str = [''] * N

for i in range(len(tate_bit)):
    merged_str[2*i] = tate_bit[i]
for i in range(len(yoko_bit)):
    merged_str[2*i+1] = yoko_bit[i]

now = 'L'
ans = []
for i in range(N):
    #print(now)
    if i%2 == 0:
        if now == 'L' and merged_str[i] == 'P':
            ans.append('L')
            now = 'U'
        if now == 'R' and merged_str[i] == 'P':
            ans.append('R')
            now = 'U'
        if now == 'L' and merged_str[i] == 'N':
            ans.append('R')
            now = 'D'
        if now == 'R' and merged_str[i] == 'N':
            ans.append('L')
            now = 'D'
    if i%2 == 1:
        if now == 'U' and merged_str[i] == 'P':
            ans.append('R')
            now = 'L'
        if now == 'D' and merged_str[i] == 'P':
            ans.append('L')
            now = 'L'
        if now == 'U' and merged_str[i] == 'N':
            ans.append('L')
            now = 'R'
        if now == 'D' and merged_str[i] == 'N':
            ans.append('R')
            now = 'R'

print("Yes")
print("".join(ans))