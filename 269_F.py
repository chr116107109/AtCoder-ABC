import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N,M = map(int,input().split())
Q = int(input())

a = []


def calc(x,y):
    if x<0 or y<0:
        return 0
    res = 0

    res += ((1+x)//2*x) * (y//2)
    print(res)
    res += (x//2)*M * ((1+y)//2*x)
    print(res)
    if x%2 == 1:
        res -= (1+(1+2*(y//2)))//2 * (y//2+1)
    print(res)
    if y%2 == 1:
        res += (1+(y-1)*M*2 + 2*(x//2))//2*(x//2+1)
    print(res)
    return res
for i in range(Q):
    A,B,C,D = map(int,input().split())

    ans = (C+D)//2*(D-C+1) * ((B-A+1)//2)
    print(ans)
    ans += ((1+B-A)//2*(B-A) * M) * ((D-C+1)//2)
    print(ans)
    if (B-A+1)%2 == 1:
        if (B+C)%2 == 0:
            if (D-C)%2 == 0:
                ans += (C+(B-A)*M + D+(B-A)*M)//2*(D-C+1)//2
            else:
                ans += (C+(B-A)*M + (D-1)+(B-A)*M)//2*(D-C)//2
        else:
            if (D-C)%2 == 0:
                ans += ((C+1)+(B-A)*M + D+(B-A)*M)//2*(D-C)//2
            else:
                ans += ((C+1)+(B-A)*M + (D-1)+(B-A)*M)//2*(D-C-1)//2

    a.append(ans)

print(*a,sep='\n')