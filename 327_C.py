import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


# A is 9*9 matrix
A = [list(map(int,input().split())) for _ in range(9)]

ok = True

"""
A の各行について、その行に含まれる 
9 マスには 
1 以上 
9 以下の整数がちょうど 
1 個ずつ書き込まれている。
"""
for i in range(9):
    if len(set(A[i])) != 9:
        ok = False

"""
A の各列について9以下の整数がちょうど 
1 個ずつ書き込まれている
"""
for i in range(9):
    if len(set([A[j][i] for j in range(9)])) != 9:
        ok = False

"""
A の行を上から 
3 行ずつ 
3 つに分け、同様に列も左から 
3 列ずつ 
3 つに分ける。 これによって 
A を 
9 つの 
3×3 のマス目に分けたとき、それぞれの 
3×3 のマス目には 
1 以上 
9 以下の整数がちょうど 
1 個ずつ書き込まれている。
"""
for i in range(3):
    for j in range(3):
        if len(set([A[3*i+k][3*j+l] for k in range(3) for l in range(3)])) != 9:
            ok = False
if ok:
    print("Yes")
else:
    print("No")
    

