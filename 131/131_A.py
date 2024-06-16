
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

S = input()

for i in range(len(S)-1):
    if S[i] == S[i+1]:
        print('Bad')
        sys.exit()
    
print('Good')
