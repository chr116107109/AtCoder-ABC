import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math


v1,v2,v3 = map(int,input().split())


N = 7

def kasanaru(a,b,c,d):
    return max(0,min(b,d) - max(a,c))


def f(i,j,k,x,y,z):
    # [0,7]x[0,7]x[0.7]の領域と
    # [i,i+7]x[j,j+7]x[k,k+7]の領域と
    # [x,x+7]x[y,y+7]x[z,z+7]の領域が重なる体積を求める

    # 全て重なる部分は　U1
    # 2つだけ重なる部分は　U2
    # 1つだけ重なる部分は　U3

    # U1の体積
    tate = min(7,i+7,x+7) - max(0,i,x) 
    yoko = min(7,j+7,y+7) - max(0,j,y)
    takasa = min(7,k+7,z+7) - max(0,k,z)

    if tate <= 0 or yoko <= 0 or takasa <= 0:
        U1 = 0
    else:
        U1 = tate * yoko * takasa

    # U2の体積

    # 1,2が重なる部分
    s12 = kasanaru(0,7,i,i+7) * kasanaru(0,7,j,j+7) * kasanaru(0,7,k,k+7)

    # 2,3が重なる部分
    s23 = kasanaru(0,7,x,x+7) * kasanaru(0,7,y,y+7) * kasanaru(0,7,z,z+7)
    
    # 3,1が重なる部分
    s31 = kasanaru(i,i+7,x,x+7) * kasanaru(j,j+7,y,y+7) * kasanaru(k,k+7,z,z+7)
    #print(s12,s23,s31)

    U2 = s12 + s23 + s31 - 3*U1

    # U3の体積
    U3 = 7*7*7*3 - 2*U2 -  3*U1

    return U1,U2,U3




for i in range(-1,N):
    for j in range(-1,N):
        for k in range(-1,N):
            for x in range(-1,N):
                for y in range(-1,N):
                    for z in range(-1,N):
                        
                        U1,U2,U3 = f(i,j,k,x,y,z)
                        if U1 == v3 and U2 == v2 and U3 == v1:
                            print('Yes')
                            print(0,0,0,i,j,k,x,y,z)
                            sys.exit()

print('No')