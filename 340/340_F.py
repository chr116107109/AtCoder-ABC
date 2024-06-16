import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math
import sys
X,Y = map(int,input().split())

D = X**2 + Y**2

a = X * D * D
b = Y * D * D
c = X*(a - 2*Y) + Y*(b + 2*X)
d = X*(a + 2*Y) + Y*(b - 2*X)
# ax+by = cの整数解を求める

from math import gcd
class LDE:
    #初期化
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c
        self.m,self.x,self.y=0,[0],[0]
        #解が存在するか
        self.check=True
        g=gcd(self.a,self.b)
        if c%g!=0:
            self.check=False
        else:
            #ax+by=gの特殊解を求める
            self.extgcd(abs(self.a),abs(self.b),self.x,self.y)
            if a<0:self.x[0]=-self.x[0]
            if b<0:self.y[0]=-self.y[0]
            #ax+by=cの特殊解を求める
            self.x=self.x[0]*c//g
            self.y=self.y[0]*c//g
            #一般解を求めるために
            self.a//=g
            self.b//=g

    #拡張ユークリッドの互除法
    #返り値:aとbの最大公約数
    def extgcd(self,a,b,x0,y0):
        if b==0:
            x0[0],y0[0]=1,0
            return a
        d=self.extgcd(b,a%b,y0,x0)
        y0[0]-=(a//b)*x0[0]
        return d

    #パラメータmの更新(書き換え)
    def m_update(self,m):
        self.x+=(m-self.m)*self.b
        self.y-=(m-self.m)*self.a
        self.m=m


def find(lde):
    # 一般解は　x = self.x + k * self.b, y = y - k * selx.a
    # 特殊解がLIMITの範囲に入ってるなら出力
    LIMIT = 10**18
    ans = -1
    if abs(lde.x) <= LIMIT and abs(lde.y) <= LIMIT:
        ans = (lde.x,lde.y)
    else:
        # |x| < LIMIT, |y| < LIMIT  となるkを求める
        # |x| = |self.x + k * self.b| < LIMIT
        # |y| = |self.y - k * self.a| < LIMIT
        # |self.x + k * self.b| < LIMIT
        # -LIMIT < self.x + k * self.b < LIMIT
        # -LIMIT - self.x < k * self.b < LIMIT - self.x
        # b > 0の時
        # (-LIMIT - self.x) / self.b < k < (LIMIT - self.x) / self.b
        # b < 0の時
        # (LIMIT - self.x) / self.b < k < (-LIMIT - self.x) / self.b
        # 同様にaについても
        # a > 0の時
        # (-LIMIT - self.y) / self.a < k < (LIMIT - self.y) / self.a
        # a < 0の時
        # (LIMIT - self.y) / self.a < k < (-LIMIT - self.y) / self.a
        
        if a > 0 and b > 0:
            k = min((LIMIT - lde.x) // lde.b, (LIMIT - lde.y) // lde.a)
        elif a > 0 and b < 0:
            k = min((LIMIT - lde.x) // lde.b, (-LIMIT - lde.y) // lde.a)
        elif a < 0 and b > 0:
            k = min((-LIMIT - lde.x) // lde.b, (LIMIT - lde.y) // lde.a)
        else:
            k = min((-LIMIT - lde.x) // lde.b, (-LIMIT - lde.y) // lde.a)
        
        if abs(lde.x + k * lde.b) <= LIMIT and abs(lde.y - k * lde.a) <= LIMIT:
            ans = (lde.x + k * lde.b, lde.y - k * lde.a)

        return ans

lde1 = LDE(a,b,c)
lde2 = LDE(a,b,d)

if lde1.check and lde2.check == False:
    print(-1)
else:
    ans = find(lde1)
    if ans == -1:
        ans = find(lde2)
    print(ans)