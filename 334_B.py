import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A,M,L,R = map(int,input().split())


'''
ある整数kについてA + kMを満たす座標に印があるとする
座標LからRまでの間に印がある座標の数を求める
'''

# まずはA + kM <= Rを満たす最大のkを求める
# これはR - AをMで割った商
k = (R - A) // M

# 次にA + kM >= Lを満たす最小のkを求める
# これはL - AをMで割った商
l = (L - A-1) // M

# このkとlの間にある整数の数が答え
print(k - l)