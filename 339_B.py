import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

H,W,N = map(int,input().split())

A = [['.']*W for _ in range(H)]

now = [[0,0],'U']

def round(pos,dir):
    if dir == 'U':
        return [(pos[0])%H,(pos[1]+1)%W], 'R'
    elif dir == 'D':
        return [(pos[0])%H,(pos[1]-1)%W], 'L'
    elif dir == 'L':
        return [(pos[0]-1)%H,(pos[1])%W], 'U'
    elif dir == 'R':
        return [(pos[0]+1)%H,(pos[1])%W], 'D'


def inverse_round(pos,dir):
    if dir == 'U':
        return [(pos[0])%H,(pos[1]-1)%W], 'L'
    elif dir == 'D':
        return [(pos[0])%H,(pos[1]+1)%W], 'R'
    elif dir == 'L':
        return [(pos[0]+1)%H,(pos[1])%W], 'D'
    elif dir == 'R':
        return [(pos[0]-1)%H,(pos[1])%W], 'U'

for i in range(N):
    pos,dir = now
    #print(pos,dir)
    if A[pos[0]][pos[1]] == '.':
        A[pos[0]][pos[1]] = '#'
        now = round(pos,dir)
    else:
        A[pos[0]][pos[1]] = '.'
        now = inverse_round(pos,dir)
    
for a in A:
    print(''.join(a))
#    print('')


