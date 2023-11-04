

A,B,W = map(int,input().split())
W *= 1000
import sys
if A > W:
    print('UNSATISFIABLE')
    sys.exit()

m = W
M = 0
for i in range(1,W+1):
    if A <= W/i <= B:
        m = min(m,i)
        M = max(M,i)

if m == W and M == 0:
    print('UNSATISFIABLE')
else:
    print(m,M)