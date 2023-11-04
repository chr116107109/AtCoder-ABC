

N,M,K = map(int,input().split())

A = [list(map(int,input().split())) for i in range(N)]
B = [list(map(int,input().split())) for i in range(M)]

d = []

import itertools

for a,b in itertools.product(A,B):
    d.append([(a[0]+b[0])/(a[0]+b[0]+a[1]+b[1]), a, b])

d.sort(key=lambda x: x[0])