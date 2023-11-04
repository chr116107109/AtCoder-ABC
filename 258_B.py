
N = int(input())
A = [input() for i in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        for k in range(8):
            if k == 0:
                s = [A[(i+l)%N][j] for l in range(N)]
            if k == 1:
                s = [A[(i)%N][(j+l)%N] for l in range(N)]
            if k == 2:
                s = [A[(i+l)%N][(j+l)%N] for l in range(N)]
            if k == 3:
                s = [A[(i-l)%N][(j+l)%N] for l in range(N)]
            if k == 4:
                s = [A[(i-l)%N][(j)%N] for l in range(N)]
            if k == 5:
                s = [A[(i)%N][(j-l)%N] for l in range(N)]
            if k == 6:
                s = [A[(i-l)%N][(j-l)%N] for l in range(N)]
            if k == 7:
                s = [A[(i+l)%N][(j-l)%N] for l in range(N)]
            
            
            
            
            ans = max(ans, int(''.join(s)))

print(ans)