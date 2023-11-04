import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


S = input()
d = {'ACE','BDF','CEG','DFA','EGB','FAC','GBD'}

if S in d:
    print('Yes')
else:
    print('No')

