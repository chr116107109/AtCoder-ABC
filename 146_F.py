import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
S = list(map(int,input()))

#####segfunc#####
def segfunc(x, y):
    return min(x,y)
#################

#####ide_ele#####
ide_ele = 10**10
#################

class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res
    

inf = 10**10

d = [inf] * (N+1)
d[0] = 0
seg = SegTree(d, segfunc, ide_ele)

dist2ele = [[] for i in range(N+1)]
dist2ele[0].append(0)
out = set()
for i in range(1,N+1):
    if S[i] == 0:
        v = seg.query(max(0,i-M),i)
        seg.update(i,v + 1)
        if v+1 > N+1:
            out.add(i)
            continue
        dist2ele[v+1].append(i)
    else:
        out.add(i)

if N in out:
    print(-1)
else:
    path = []
    now = N
    while v >= 0:
        i = bisect_left(dist2ele[v],now-M)
        path.append(now - dist2ele[v][i])
        now = dist2ele[v][i]
        v -= 1
    path.reverse()
    print(*path)