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



N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
from collections import Counter
A = [(a[i],b[i]) for i in range(N)]
A = list(set(A))
B = Counter()
for i in range(N):
    B[(a[i],b[i])] += 1


A.sort(key=lambda x:x[0]*10**10-x[1])

q = OrderBIT([a[1] for a in A])

import math

count = 0
ans = 0
for i in range(len(A)):
    count += B[(A[i][0],A[i][1])]
    ans += (count - q.count_lower(A[i][1]-0.5))*B[(A[i][0],A[i][1])] #+ B[(A[i][0],A[i][1])]*(B[(A[i][0],A[i][1])]-1)
    #print(ans,A[i],q.count_lower(A[i][1]-0.5),count)
    q.insert_val(A[i][1],B[(A[i][0],A[i][1])])

print(ans)