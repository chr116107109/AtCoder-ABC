
N = int(input())

import math
ans = 0
for i in range(1,N):

    M = int(math.sqrt(i))

    S = set()
    for j in range(1,M + 1):
        if i%j == 0:
            S.add((i//j,j))
            S.add((j,i//j))
    
    coun_ab = len(S)
    MM = int(math.sqrt(N-i))
    for j in range(1,MM + 1):
        if (N-i)%j == 0:
            #print(N-i,j)
            if ((N-i)//j,j) in S:
                ans += coun_ab
            else:
                ans += coun_ab
            
            if (N-i)//j == j:
                continue
            if (j,(N-i)//j) in S:
                ans += coun_ab
            else:
                ans += coun_ab

    #print(S,ans)

print(ans)