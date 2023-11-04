
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

import itertools 

s = []
for a in itertools.permutations(range(1,N+1)):
    s.append(list(a))

s.sort()

for i,t in enumerate(s):
    if t == P:
        a = i
    if t == Q:
        b = i

print(abs(a-b))