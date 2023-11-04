############################################################################
# オイラーツアー
# dfsで頂点に入った時と戻ってきた時を記録する
# 部分木についてなんかしたい時によく使う

visited = {}
ot = []
inout = [[0,0] for i in range(N)]
def dfs(s,d):
    if len(g[s]) == 1 and s != 0:
        visited[s] = d
        inout[s][0] = len(ot)
        ot.append(s)
        inout[s][1] = len(ot)
        ot.append(s)
        return
    
    visited[s] = d
    inout[s][0] = len(ot)
    ot.append(s)
    for t in g[s]:
        if t in visited:
            continue
        dfs(t,d+1)
    inout[s][1] = len(ot)
    ot.append(s)

    return

############################################################################
# 遅延セグメント木
# 区間更新と区間クエリをlogNでできる

INF = 2**31-1

LV = (N-1).bit_length()
N0 = 2**LV
data = [INF]*(2*N0)
lazy = [None]*(2*N0)

# 伝搬対象の区間を求める
def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1

# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if v is None:
            continue
        lazy[2*i-1] = data[2*i-1] = lazy[2*i] = data[2*i] = v
        lazy[i-1] = None

# 区間[l, r)をxで更新
def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)

    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] = data[R-1] = x
        if L & 1:
            lazy[L-1] = data[L-1] = x
            L += 1
        L >>= 1; R >>= 1
    for i in ids:
        data[i-1] = min(data[2*i-1], data[2*i])

# 区間[l, r)内の最小値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r

    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])
        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

############################################################################

# 強連結成分分解(SCC): グラフGに対するSCCを行う
# 入力: <N>: 頂点サイズ, <G>: 順方向の有向グラフ, <RG>: 逆方向の有向グラフ
# 出力: (<ラベル数>, <各頂点のラベル番号>)
def scc(N, G, RG):
    order = []
    used = [0]*N
    group = [None]*N
    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)
    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0]*N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return label, group

# 縮約後のグラフを構築
def construct(N, G, label, group):
    G0 = [set() for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].add(lbt)
        GP[lbs].append(v)
    return G0, GP

####################################################################
# 全てのループを集めておく

g = [[set(),set()] for i in range(N)]
g_ori = [[set(),set()] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    g[a-1][0].add(b-1)
    g[b-1][1].add(a-1)
    g_ori[a-1][0].add(b-1)
    g_ori[b-1][1].add(a-1)


def get_loop(g):
    q = []
    visited = set()
    for i in range(N):
        if g[i][1] == set():
            q.append(i)

    while q:
        s = q.pop()
        visited.add(s)
        for t in g[s][0]:
            g[t][1].remove(s)
            if g[t][1] == set():
                q.append(t)
    
    q = []
    for i in range(N):
        if g[i][0] == set():
            q.append(i)

    while q:
        s = q.pop()
        visited.add(s)
        for t in g[s][1]:
            g[t][0].remove(s)
            if g[t][0] == set():
                q.append(t)

    return visited

####################################################################
# ワーシャル・フロイド法　O(V^3) 任意の２点間の最短距離　（重りあり）
def WFM(d,N,M):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])                    

    return d

####################################################################
# BFS O(V) uからの最短距離　（重みなし）
from collections import deque
def bfs(u):
    queue = deque([u])
    d = [None] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

####################################################################
# DFS 
from collections import deque
time = 0
arrive_time = [-1] * (N + 1) # 到着時刻
finish_time = [-1] * (N + 1) # 探索終了時刻
def dfs(v):
    global time
    time += 1
    stack = [v]
    arrive_time[v] = time
    while stack:
        v = stack[-1]
        if graph[v]:
            w = graph[v].popleft()
            if arrive_time[w] < 0:
                time += 1
                arrive_time[w] = time
                stack.append(w) 
        else:
            time += 1
            finish_time[v] = time
            stack.pop()          
    return [arrive_time, finish_time]



####################################################################
# 再帰
def dfs(x,y):
    if not(0 <= x < h) or not(0 <= y < w) or c[x][y] == "#": # 壁に当たったり、探索範囲外になった場合はreturn
        return
    if c[x][y] == "g": # ゴールを見つけたら”Yes”を出力して終了
        print("Yes")
        sys.exit()
        
    c[x][y] = "#" #探索済みを示すためのマーキング
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)

#######################################################################
# bit全探索
for i in range(2 ** n):
    bag = []
    print("pattern {}: ".format(i), end="")
    for j in range(n):  # このループが一番のポイント
        if ((i >> j) & 1):  # 順に右にシフトさせ最下位bitのチェックを行う
            bag.append(item[j][0])  # フラグが立っていたら bag に果物を詰める
    print(bag)

#######################################################################
# 素数列挙、素因数分解
def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] != 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = 0

    primes = sorted(list(set(nums)))[2:]

    return primes

P = sieve_of_eratosthenes(max(A))
def factorization(n,P):
    arr = {}
    temp = n
    for i in P:
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if arr=={}:
        arr[n] = 1

    return arr

#######################################################################
# 素数列挙、高速素因数分解

def sieve_of_eratosthenes(x):
    nums = [i for i in range(x+1)]

    root = int(pow(x,0.5))
    for i in range(2,root + 1):
        if nums[i] > 0:
            for j in range(i, x+1):
                if i*j >= x+1:
                    break
                nums[i*j] = -i

    return nums

P = sieve_of_eratosthenes(max(A))
p_set = set()

is_pc = True

for i in range(N):
    a = A[i]
    while a > 1:
        if P[a] < 0:
            p = -P[a]
        else:
            p = P[a]
        while a%p == 0:
            a //= p

####################################################################
# combination 前計算

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return ((g1[n] * g2[r])%mod * g2[n-r]) % mod

mod = 10**9+7 #出力の制限
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )


####################################################################

class Factorial():
    def __init__(self, mod=10**9 + 7):
        self.mod = mod
        self._factorial = [1]
        self._size = 1
        self._factorial_inv = [1]
        self._size_inv = 1
    
    def __call__(self, n):
        '''n! % mod '''
        return self.fact(n)
    
    def fact(self, n):
        '''n! % mod '''
        if n >= self.mod:
            return 0
        self.make(n)
        return self._factorial[n]
    
    def fact_inv(self, n):
        '''n!^-1 % mod '''
        if n >= self.mod:
            raise ValueError('Modinv is not exist! arg={}'.format(n))
        self.make_inv(n)
        return self._factorial_inv[n]
    
    def comb(self, n, r):
        ''' nCr % mod '''
        if r > n:
            return 0
        t = self.fact_inv(n-r)*self.fact_inv(r) % self.mod
        return self(n)*t % self.mod
    
    def comb_with_repetition(self, n, r):
        ''' nHr % mod '''
        t = self.fact_inv(n-1)*self.fact_inv(r) % self.mod
        return self(n+r-1)*t % self.mod
    
    def perm(self, n, r):
        ''' nPr % mod '''
        if r > n:
            return 0
        return self(n)*self.fact_inv(n-r) % self.mod
    
    @staticmethod
    def xgcd(a, b):
        ''' return (g, x, y) such that a*x + b*y = g = gcd(a, b) '''
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0
    
    def modinv(self, n):
        g, x, _ = self.xgcd(n, self.mod)
        if g != 1:
            raise ValueError('Modinv is not exist! arg={}'.format(n))
        return x % self.mod
    
    def make(self, n):
        if n >= self.mod:
            n = self.mod
        if self._size < n+1:
            for i in range(self._size, n+1):
                self._factorial.append(self._factorial[i-1]*i % self.mod)
            self._size = n+1
    
    def make_inv(self, n):
        if n >= self.mod:
            n = self.mod
        self.make(n)
        if self._size_inv < n+1:
            for i in range(self._size_inv, n+1):
                self._factorial_inv.append(self.modinv(self._factorial[i]))
            self._size_inv = n+1

####################################################################
# 拡張GCD

# Euclidean Algorithm
def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

# Euclidean Algorithm (non-recursive)
def gcd2(m, n):
    while n:
        m, n = n, m % n
    return m

# Extended Euclidean Algorithm
def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

# lcm (least common multiple)
def lcm(m, n):
    return m//gcd(m, n)*n


####################################################################
# 順序付き集合　
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

######################################################
# binary indexed tree
# 値の追加と総和がlogNでできる
# add(i,x): i番目に+x
# sum(i): i番目にまでの和

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
