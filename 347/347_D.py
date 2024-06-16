import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right
from heapq import heappush,heappop
import itertools
import math

a,b,C = map(int,input().split())

c_bit = bin(C)[2:]

def popcount(x):
    x_bit = bin(x)[2:]
    return x_bit.count("1")

X_bit = ""
Y_bit = ""

X_bit = ["0"]*len(c_bit)
Y_bit = ["0"]*len(c_bit)
for i in range(len(c_bit)):
    bit = c_bit[i]
    if bit == "1":
        if a == 0 and b == 0:
            print(-1)
            sys.exit()
        if a >= b:
            X_bit[i] = "1"
            Y_bit[i] = "0"
            a -= 1
        else:
            X_bit[i] = "0"
            Y_bit[i] = "1"
            b -= 1
for i in range(len(c_bit)):
    if c_bit[i] == "0":
        if a > 0 and b > 0:
            X_bit[i] = "1"
            Y_bit[i] = "1"
            a -= 1
            b -= 1
        else:
            X_bit[i] = "0"
            Y_bit[i] = "0"

if a == b:
    X = int("1"*a + "".join(X_bit),2)
    Y = int("1"*b + "".join(Y_bit),2)
    if X < pow(2,60) and Y < pow(2,60):
        print(X,Y)
    else:
        print(-1)
else:
    print(-1)