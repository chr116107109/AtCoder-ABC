
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N = int(input())
uf=UnionFind(N)
d = [deque() for i in range(N)]
for i in range(N):
    d[i].append([i,0])

mod=998244353

root2list = list(range(N))
for i in range(N-1):
    p,q = map(int,input().split())
    p -= 1
    q -= 1
    p_ind = root2list[uf.find(p)]
    q_ind = root2list[uf.find(q)]
    
    n_p = uf.size(p)
    n_q = uf.size(q)
    p_rate = (n_p * pow(n_p+n_q, mod-2, mod)) %mod
    q_rate = (n_q * pow(n_p+n_q, mod-2, mod)) %mod
    uf.union(p,q)
    if n_p > n_q:    
        d[p_ind].appendleft([-1,p_rate])
        d[p_ind].append([-1,-p_rate])
        d[p_ind].appendleft([-1,-q_rate])
        while d[q_ind]:
            d[p_ind].appendleft(d[q_ind].pop())
        d[p_ind].appendleft([-1,q_rate])

        root2list[uf.find(p)] = p_ind

    else:
        d[q_ind].appendleft([-1,q_rate])
        d[q_ind].append([-1,-q_rate])
        d[q_ind].append([-1,p_rate])
        while d[p_ind]:
            d[q_ind].append(d[p_ind].popleft())
        d[q_ind].append([-1,-p_rate])

        root2list[uf.find(q)] = q_ind

    #print(d)

root = root2list[uf.find(0)]
now = 0
ans = [0] * N
while d[root]:
    ind, s = d[root].popleft()
    now += s
    now %= mod
    if ind > -1:
        ans[ind] = now

print(*ans)