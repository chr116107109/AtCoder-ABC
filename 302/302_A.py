

import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right

A,B = map(int,input().split())

if A%B == 0:
    print(A//B)
else:
    print(A//B+1)

