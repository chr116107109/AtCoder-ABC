
import sys

[N,M] = map(int,input().split())

B = [list(map(int,input().split())) for i in range(N)]


base = [B[0][0] // 7 , (B[0][0]-1) % 7 ]

if M > (7 - base[1]):
    print('No')
    sys.exit()


for i in range(N):
    for j in range(M):
        if B[i][j] == B[0][0] + 7*i + j:
            continue
        else:
            print('No')
            sys.exit()

print('Yes')
