

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


N,M,Q = map(int,input().split())

X = []
# i番目の出力を計算するのに必要なのは、最後に行更新が入ったクエリ番号をkとした時のSkと更新値x
index2beforeindex = {}
before_x = [[0,0] for i in range(N)] # [x,index]
outputs = {}
last_update_index2output = defaultdict(list)
for i in range(Q):
    q = list(map(int,input().split()))
    X.append(q)
    if q[0] == 2:
        before_x[q[1]-1] = [q[2], i]
    if q[0] == 3:
        outputs[i] = before_x[q[1]-1][0]
        if before_x[q[1]-1][1] != 0:
            last_update_index2output[before_x[q[1]-1][1]].append(i)
    

BT = Bit(M+2)
for i in range(Q):
    if i in last_update_index2output:
        for index in last_update_index2output[i]:
            outputs[index] -= BT.sum(X[index][2]) # Sk 値を引く
    
    if X[i][0] == 1:
        _,l,r,x = X[i]
        BT.add(l, x)
        BT.add(r+1, -x)
    if X[i][0] == 3:
        _,I,J = X[i]
        outputs[i] += BT.sum(J)
        print(outputs[i])

    #print([BT.sum(i) for i in range(N+2)])
    #print(outputs)