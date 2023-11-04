
N,A,B = map(int,input().split())
S = input()
ans = 10**20

for i in range(N):
    count = 0
    for j in range(N//2):
        if S[(i+j)%N] != S[(i+N-j-1)%N]:
            count += 1
    ans = min(ans, A*i+count*B)

print(ans)