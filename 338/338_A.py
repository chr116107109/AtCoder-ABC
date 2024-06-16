import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

if S[0].isupper():
    if len(S) == 1:
        print("Yes")
    else:   
        if S[1:].islower():
            print("Yes")
        else:
            print("No")
else:
    print("No")