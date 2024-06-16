import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

N = int(input())
S = list(input().split())

node = ['root']
edges = [{}]

value = [0]

ans = 0
for i in range(N-1,-1,-1):
    s = S[i]

    now_node = 0
    now_ind = 0
    for j in range(len(s)):
        
        now_str = s[now_ind]
        if now_str in edges[now_node]:

            
            ans += value[edges[now_node][now_str]] + 1
            value[edges[now_node][now_str]] += 1

        else:
            edges[now_node][now_str] = len(edges)
            edges.append({})
            value.append(0)
            node.append(now_str)

        now_node = edges[now_node][now_str]
        now_ind += 1
    #print(s)
    #print(node)
    #print(edges)
    ##print(value)
    #print(ans)


print(ans)