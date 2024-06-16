

N = int(input())
p = list(map(int,input().split()))

d = [0] * N
for i in range(N):
    d[(i-p[i]-1)%N] += 1
    d[(i-p[i])%N] += 1
    d[(i-p[i]+1)%N] += 1
    #print(p[i],d)

print(max(d))