
S = input()
N = int(input())

M = len(S)

ans = 0
for i in range(M):
    if S[i] == '1':
        N -= pow(2,M-i-1)
        ans += pow(2,M-i-1)

import sys
if N < 0:
    print(-1)
    sys.exit()

for i in range(M):
    if S[i] == '?':
        if N >= pow(2,M-i-1):
            N -= pow(2,M-i-1)
            ans += pow(2,M-i-1)
    

print(ans)