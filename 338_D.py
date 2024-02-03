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
        self.tree = [0]*(n+1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

class BitImos:
    """
    ・範囲すべての要素に加算
    ・ひとつの値を取得
    の2種類のクエリをO(logn)で処理
    """
    def __init__(self, n):
        self.bit = Bit(n+1)

    def add(self, s, t, x):
        # [s, t)にxを加算
        self.bit.add(s, x)
        self.bit.add(t, -x)

    def get(self, i):
        return self[i]

    def __getitem__(self, key):
        # 位置iの値を取得
        return self.bit.sum(key+1)
    

N,M = map(int,input().split())
A = list(map(int,input().split()))

B = BitImos(N+1)
Count = BitImos(N+1)

init_ans = 0
# 初期回
for i in range(M-1):
    if abs(A[i] - A[i+1]) <= N//2:
        B.add(min(A[i]-1,A[i+1]-1),max(A[i]-1,A[i+1]-1), abs(A[i] - A[i+1]))
        Count.add(min(A[i]-1,A[i+1]-1),max(A[i]-1,A[i+1]-1), 1)

        #print(A[i]-1,A[i+1]-1, abs(A[i] - A[i+1]))
        init_ans += abs(A[i] - A[i+1])
    else:
        B.add(0,min(A[i+1]-1,A[i]-1), N - abs(A[i] - A[i+1]))
        B.add(max(A[i+1]-1,A[i]-1),N, N - abs(A[i] - A[i+1]))
        
        Count.add(0,min(A[i+1]-1,A[i]-1), 1)
        Count.add(max(A[i+1]-1,A[i]-1),N, 1)

        init_ans += N - abs(A[i] - A[i+1])
        #xprint(0,min(A[i+1]-1,A[i]-1), N - abs(A[i] - A[i+1]))

    #for i in range(N):
    #    print(B.get(i),end=" ")

    #print()
ans = 10**10
for i in range(N):

    tmp =  init_ans + (Count.get(i)*N - 2*B.get(i))
    ans = min(ans,tmp)
    #print(tmp)

print(ans)