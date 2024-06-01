import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


N, L, R = map(int,input().split())

ans = 0

while L <= R:
    #print(L,R)
    # Lの経っているbitで最小のもの
    if L == 0:
        L_min = 60
    else:
        for i in range(60):
            if (L >> i) & 1:
                L_min = i
                break

    
    while L + (1 << L_min) - 1 > R:
        L_min -= 1

    i = L_min
    j = L//pow(2,i)

    print("?",i,j,flush=True)
    #print("debug","L",j*pow(2,i),"R",(j+1)*pow(2,i)-1,flush=True)
    res = int(input())
    if res == -1:
        sys.exit()
    L += pow(2,i)
    ans += res
    ans %= 100


print("!",ans)
