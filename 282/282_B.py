
import itertools


N,M = map(int,input().split())
S = [input() for i in range(N)]

ans = 0
for i,j in itertools.combinations(range(N),2):
    a = 1
    for k in range(M):
        if S[i][k] == 'o' or S[j][k] == 'o':
            continue
        else:
            a = 0
            break
    
    ans += a

print(ans)