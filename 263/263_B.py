
N = int(input())
P = list(map(int,input().split()))

d = [0] * N

for i in range(1,N):
    d[i] = d[P[i-1]-1] + 1

print(d[N-1])