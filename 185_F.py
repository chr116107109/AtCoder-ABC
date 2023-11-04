

N,Q = map(int,input().split())
A = list(map(int,input().split()))

class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s ^= self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] ^= x
            i += i & -i


p = Bit(N)
for i in range(N):
    p.add(i+1,A[i])

#print([p.sum(i) for i in range(1,N+1)])

for i in range(Q):
    t,x,y =  map(int,input().split())
    
    if t == 1:
        p.add(x,y)
    else:
        print(p.sum(y)^p.sum(x-1))
