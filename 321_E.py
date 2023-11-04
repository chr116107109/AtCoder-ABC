import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

T = int(input())

INF = 10**20
def left(X,K):
    if K > 70:
        return INF
    return X*pow(2,K)

def right(X,K):
    Y = X
    if K > 70:
        return INF
    for i in range(K):
        Y *= 2
        Y += 1
    return Y

def calc_child_K(N,K,X):
    l = left(X,K)
    r = right(X,K)
    return max(min(r,N) - l + 1, 0)

def main(N,K,X):
    count = calc_child_K(N,K,X)
    
    if K < 70 and X >= pow(2,K) and K != 0:
        count += 1
    K -= 2
    while X > 1 and K >= 0:
        #print(X,K)
        #print(i,X,K,count)
        if X % 2 == 0:
            tonari = X + 1
        else:
            tonari = X - 1
    
        count += calc_child_K(N,K,tonari)
        X //= 2
        K -= 1
    
    return count

ans = []
for i in range(T):
    N,X,K = map(int,input().split())

    ans.append(main(N,K,X))

print(*ans, sep='\n')


sys.exit()
import random
while True:
    N = random.randint(2,10**18)
    X = random.randint(1,N)
    K = random.randint(1,N-1)
    print(N,K,X)
    main(N,K,X)

