import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


def segfunc(x,y):
    return min(x,y)
class LazySegTree_RUQ:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)
        self.n = n
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1<<(n-1).bit_length()
        self.tree = [ide_ele]*2*self.num
        self.lazy = [None]*2*self.num
        for i in range(n):
            self.tree[self.num+i] = init_val[i]
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])
    def gindex(self,l,r):
        l += self.num
        r += self.num
        lm = l>>(l&-l).bit_length()
        rm = r>>(r&-r).bit_length()
        while r>l:
            if l<=lm:
                yield l
            if r<=rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1
    def propagates(self,*ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            self.lazy[2*i] = v
            self.lazy[2*i+1] = v
            self.tree[2*i] = v
            self.tree[2*i+1] = v
    def update(self,l,r,x):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r&1:
                self.lazy[r-1] = x
                self.tree[r-1] = x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2*i], self.tree[2*i+1])
    def query(self,l,r):
        ids = self.gindex(l,r)
        self.propagates(*self.gindex(l,r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res
    
    def debug(self):
        a = []
        for i in range(self.n):
            a.append(self.query(i,i+1))
        print("seg debug",*a)
    
import bisect

class BIT:

    def __init__(self,len_A):
        self.N = len_A + 10
        self.bit = [0]*(len_A+10)
        
    # sum(A0 ~ Ai)
    # O(log N)
    def query(self,i):
        res = 0
        idx = i+1
        while idx:
            res += self.bit[idx]
            idx -= idx&(-idx)
        return res

    # Ai += x
    # O(log N)
    def update(self,i,x):
        idx = i+1
        while idx < self.N:
            self.bit[idx] += x
            idx += idx&(-idx)
    
    # min_i satisfying {sum(A0 ~ Ai) >= w} (Ai >= 0)
    # O(log N)
    def lower_left(self,w):
        if (w < 0):
            return -1
        x = 0
        k = 1<<(self.N.bit_length()-1)
        while k > 0:
            if x+k < self.N and self.bit[x+k] < w:
                w -= self.bit[x+k]
                x += k
            k //= 2
        return x


class OrderBIT: 

    def __init__(self,all_values,sort_flag = False):
        if sort_flag:
            self.A = all_values
        else:
            self.A = sorted(all_values)
        self.B = BIT(len(all_values))
        self.num = 0
        
    def insert_val(self,x,c=1):
        k = bisect.bisect_left(self.A,x)
        self.B.update(k,c)
        self.num += c
    
    def delete_val(self,x,c=1):
        k = bisect.bisect_left(self.A,x)
        self.B.update(k,-c)
        self.num -= c
    
    # find the k-th min_val (k:0-indexed)
    def find_kth_val(self,k):
        if self.num <= k:
            ##### MINIMUM VAL #######
            return -10**9
        return self.A[self.B.lower_left(k+1)]
    
    # count the number of values lower than or equal to x
    def count_lower(self,x):
        if x < self.A[0]:
            return 0
        return self.B.query(bisect.bisect_right(self.A,x)-1)

    # min_val higher than x
    def find_higher(self,x):
        return self.find_kth_val(self.count_lower(x))
    
    # max_val lower than x
    def find_lower(self,x):
        return self.find_kth_val(self.count_lower(x)-1)

Q,K = map(int,input().split())
q = []
d = set()
for i in range(Q):
    q.append(list(map(int,input().split())))
    d.add(q[i][1])
bit = OrderBIT(list(d) + [-10**18,10**18])

pos_seg = LazySegTree_RUQ([10**18] * len(d),segfunc,10**18)
length_seg = LazySegTree_RUQ([10**18] * len(d),segfunc,10**18)

exist = set()
val2index = {}
d = sorted(list(d)  + [-10**18,10**18])
for i,x in enumerate(d):    
    val2index[x] = i

bit.insert_val(-10**18)
bit.insert_val(10**18)

for i in range(Q):
    a,x = q[i]

    if a == 1:
        if x in exist:
            
            left = bit.find_lower(x)
            right = bit.find_higher(x)

            x_ind = val2index[x]
            pos = pos_seg.query(x_ind,x_ind+1)
            length = length_seg.query(x_ind,x_ind+1)

            if x - left > K and right - x > K:
                exist.remove(x)
                bit.delete_val(x)
            else:
                pos_seg.update(pos,x_ind-1,pos)
                pos_seg.update(x_ind+1,pos+length,x_ind+1)

                length_seg.update(pos,x_ind-1,x_ind-1-pos)
                length_seg.update(x_ind+1,pos+length,pos+length-x_ind-1)

                exist.remove(x)
                bit.delete_val(x)
        else:

            left = bit.find_lower(x)
            right = bit.find_higher(x)
            x_ind = val2index[x]
            
            if x - left > K and right - x > K:
                exist.add(x)
                bit.insert_val(x)
                pos_seg.update(x_ind,x_ind+1,x_ind)
                length_seg.update(x_ind,x_ind+1,1)
                continue
            x_pos = pos_seg.query(x_ind,x_ind+1)
            x_length = length_seg.query(x_ind,x_ind+1)
            exist.add(x)
            bit.insert_val(x)
                
            if x - left <= K:
                left_ind = val2index[left]
                left_pos = pos_seg.query(left_ind,left_ind+1)
                left_length = length_seg.query(left_ind,left_ind+1)

                pos_seg.update(left_pos, left_pos + x_length + left_length, left_pos)
                length_seg.update(left_pos, left_pos + x_length + left_length, x_length + left_length)
            
            x_pos = pos_seg.query(x_ind,x_ind+1)
            x_length = length_seg.query(x_ind,x_ind+1)
            
            if right - x <= K:
                right_ind = val2index[right]
                right_pos = pos_seg.query(right_ind,right_ind+1)
                right_length = length_seg.query(right_ind,right_ind+1)

                pos_seg.update(x_pos, x_pos + right_length + x_length, x_pos)
                length_seg.update(x_pos, x_pos + right_length + x_length, right_length + x_length)

    if a == 2:
        ind = val2index[x]
        a = length_seg.query(ind,ind+1)
        print(a)

    pos_seg.debug()
    length_seg.debug()