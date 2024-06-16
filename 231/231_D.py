
import sys
sys.setrecursionlimit(10**6)

[N,Q] = list(map(int,input().split()))

def find(p,h):
    if p[h] == -1:
        return h

    else:
        p[h] = find(p,p[h])
        return p[h]

def union(p,a,b):
    fa = find(p,a)
    fb = find(p,b)

    if fa == fb:
        return [fa,fb]
    p[fa] = fb
    if fa != fb:
        return [fa,fb]


p = [-1] * (N)
asi = [0] * (N)

frag = 0
for i in range(Q):
    [a,b] = list(map(int,input().split()))

    asi[a-1] += 1
    asi[b-1] += 1

    [fa,fb] = union(p,a-1,b-1)
    #print(p)
    if fa == fb:
        frag = 1
    elif asi[a-1] >= 3 or asi[b-1] >= 3:
        frag = 1

if frag == 1:
    print('No')
else:
    print('Yes')
