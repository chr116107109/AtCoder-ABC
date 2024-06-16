import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

A,B,C,D = map(int,input().split())

ans = B - A + 1
ans -= B//C - (A-1)//C
ans -= B//D - (A-1)//D
d = math.gcd(C,D)*(D//math.gcd(C,D))*(C//math.gcd(C,D))
ans += B//(d) - (A-1)//(d)

print(ans)