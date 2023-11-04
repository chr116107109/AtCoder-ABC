
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

Q = int(input())
q = []
S = set()
for i in range(Q):
    query = list(map(int,input().split()))
    q.append(query)
    if query[0] == 1:
        S.add(query[1])

liS = list(S)
T = OrderBIT(liS)
H = OrderBIT([-s for s in liS])
l = 0

for i in range(Q):
    if q[i][0] == 1:
        x = q[i][1]
        T.insert_val(x,1)
        H.insert_val(-x,1)
    if q[i][0] == 2:
        x = q[i][1]
        c = q[i][2]
        n_x = T.count_lower(x) - T.count_lower(x-1)
        T.delete_val(x,min(n_x,c))
        H.delete_val(-x,min(n_x,c))
    if q[i][0] == 3:    
        print(-T.find_kth_val(0)-H.find_kth_val(0))
    #print('leght {}'.format(l))
    #print(T.find_kth_val(l-1),T.find_kth_val(0))
#    print(T.find_kth_val(0))






