
N = int(input())
S = []
for i in range(N):
    S = S + [i+1] + S[::-1]
print(*S)