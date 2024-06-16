
N,M = map(int,input().split())
A,B,C,D,E,F = map(int,input().split())
G = [(A,B),(C,D),(E,F)]
Z = set()
for i in range(M):
    X,Y = map(int,input().split())
    Z.add((X,Y))

mod = 998244353

before = {0:1}
after = {}

for i in range(N):
    after = {}
    for kk in before:
        k = kk
        a = k//(301**2)
        k %= (301**2)
        b = k//(301)
        k %= (301)
        c = k

        x = G[0][0]*c + G[1][0]*b + G[2][0]*a
        y = G[0][1]*c + G[1][1]*b + G[2][1]*a
        #print(x,y)
        for j,(s,t) in enumerate(G):
            if not (x+s,y+t) in Z:
                l = kk+(301**j)
                if l in after:
                    after[l] += before[kk]
                    after[l] %= mod
                else:
                    after[l] = before[kk]
        #print(before)
        #print(after)
    before = after

ans = 0
for _ in after: 
    ans += after[_]
    ans %= mod

print(ans)