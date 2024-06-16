import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math



A = [list(map(int,input().split())) for _ in range(3)]

def check(red):
    if 0 in red and 1 in red and 2 in red:
        return True
    if 3 in red and 4 in red and 5 in red:
        return True
    if 6 in red and 7 in red and 8 in red:
        return True
    if 0 in red and 3 in red and 6 in red:
        return True
    if 1 in red and 4 in red and 7 in red:
        return True
    if 2 in red and 5 in red and 8 in red:
        return True
    if 0 in red and 4 in red and 8 in red:
        return True
    if 2 in red and 4 in red and 6 in red:
        return True
    return False

def score(red):
    s = 0
    for a in red:
        i,j = a//3,a%3
        s += A[i][j]
    return s

def solve(red,blue,depth):
    #print(red,blue)
    if check(red):
        return 'red'
    if check(blue):
        return 'blue'
    if len(red) + len(blue) == 9:
        if score(red) >= score(blue):
            return 'red'
        else:
            return 'blue'
        

    if depth % 2 == 0:
        for i in range(9):
            if i in red or i in blue:
                continue
            r = red.copy()
            r.add(i)
            if solve(r,blue,depth+1) == 'red':
                return 'red'
        return 'blue'
    else:
        for i in range(9):
            if i in red or i in blue:
                continue
            b = blue.copy() 
            b.add(i)
            if solve(red,b,depth+1) == 'blue':
                return 'blue'
        return 'red'
    
if solve(set(),set(),0) == 'red':
    print('Takahashi')
else:
    print('Aoki')        