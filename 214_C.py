
N = int(input())

S = list(map(int,input().split()))
T = list(map(int,input().split()))

now = 0
mint = 10*10
for i in range(N):
    if mint > T[i]:
        now = i
        mint = T[i]

for i in range(2*N):
    now += 1
    now %= N
    T[now] = min(T[(now-1)%N]+S[(now-1)%N], T[now])

for a in T:
    print(a)