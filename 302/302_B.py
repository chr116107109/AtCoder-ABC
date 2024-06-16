
import sys
sys.setrecursionlimit(10**7)
from collections import deque,Counter,defaultdict
from bisect import bisect_left,bisect_right

H,W = map(int,input().split())
S = [input() for i in range(H)]

for i in range(H):
    for j in range(W-4):
        if S[i][j:j+5] == 'snuke':
            for k in range(5):
                print(i+1,j+k+1)
            sys.exit()
        if S[i][j:j+5] == 'ekuns':
            for k in range(4,-1,-1):
                print(i+1,j+k+1)
            sys.exit()

for j in range(W):
    for i in range(H-4):
        s = ''
        for k in range(5):
            s += S[i+k][j]
        if s == 'snuke':
            for k in range(5):
                print(i+k+1,j+1)
            sys.exit()
        if s == 'ekuns':
            for k in range(4,-1,-1):
                print(i+k+1,j+1)
            sys.exit()


for i in range(H-4):
    for j in range(W-4):
        s = ''
        for k in range(5):
            s += S[i+k][j+k]
        if s == 'snuke':
            for k in range(5):
                print(i+k+1,j+k+1)
            sys.exit()
        if s == 'ekuns':
            for k in range(4,-1,-1):
                print(i+k+1,j+k+1)
            sys.exit()

for i in range(H-4):
    for j in range(4,W):
        s = ''
        for k in range(5):
            s += S[i+k][j-k]
        if s == 'snuke':
            for k in range(5):
                print(i+k+1,j-k+1)
            sys.exit()
        if s == 'ekuns':
            for k in range(4,-1,-1):
                print(i+k+1,j-k+1)
            sys.exit()


