
S = [input() for i in range(9)]

porn = []
for i in range(9):
    for j in range(9):
        if S[i][j] == '#':
            porn.append([i,j])

import itertools
from operator import is_

def is_square(i,j,k,l):
    for a,b,c,d in itertools.permutations([i,j,k,l]):
        ll = (a[0]-b[0])**2 + (a[1]-b[1])**2
        if ll == (b[0]-c[0])**2 + (b[1]-c[1])**2 and ll == (c[0]-d[0])**2 + (c[1]-d[1])**2 and ll == (d[0]-a[0])**2 + (d[1]-a[1])**2:
            if (b[0]-a[0])*(d[0]-a[0]) + (b[1]-a[1])*(d[1]-a[1]) == 0:
                return True
    return False
ans = 0
for i,j,k,l in itertools.combinations(porn,4):
    if is_square(i,j,k,l):
        ans += 1

print(ans)