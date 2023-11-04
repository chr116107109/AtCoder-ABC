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



import sys
sys.setrecursionlimit(10**6)

[N,Q] = list(map(int,input().split()))
X = list(map(int,input().split()))

g = [[] for i in range(N)]
for i in range(N-1):
    A,B = map(int,input().split())
    g[A-1].append(B-1)
    g[B-1].append(A-1)

parent = [-1] * N
q = []
q.append(0)
while q:
    s = q.pop()
    for t in g[s]:
        if parent[t] > -1 or t == 0:
            continue
        parent[t] = s
        q.append(t)

sun = [[] for i in range(N)]

def dfs(s,K):
    if len(g[s])==1 and s > 0:
        sun[s] = [X[s]]
        return [X[s]]
    b = [X[s]]
    for t in g[s]:
        if parent[t] != s:
            continue
        b += dfs(t,K)
    b.sort()
    sun[s] = b[-K:]
    return b[-K:]

dfs(0,20)
for i in range(Q):
    V,K = map(int,input().split())
    print(sun[V-1][-K])
    



