import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())

ans = 0
mod = 998244353
for i in range(61):

    if M & (1 << i) != 0:
        #bitが立っているとき
        
        a = pow(2,i+1)
        b = (N+1)//a
        ans += b * pow(2,i)
        ans += max(0,(N+1)%a - pow(2,i))
        ans %= mod  
    
        #print(a,b,ans)

print(ans)