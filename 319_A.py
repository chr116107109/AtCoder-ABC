import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


S = input()

d = {
    'tourist': 3858,
    'ksun48': 3679,
    'Benq': 3658,
    'Um_nik': 3648,
    'apiad': 3638,
    'Stonefeang': 3630,
    'ecnerwala': 3613,
    'mnbvmar': 3555,
    'newbiedmy': 3516,
    'semiexp': 3481,
}

print(d[S])