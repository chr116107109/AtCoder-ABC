

import sys
sys.setrecursionlimit(10**6)

N = int(input())
A = [list(map(int,input().split())) for i in range(2*N-1)]

def logic_sum(a,b):
    la = format(a, '035b')
    lb = format(b, '035b')

    s = ''
    for i in range(35):
        if la[i] == lb[i]:
            s += '0'
        else:
            s += '1'

    return int(s,2)

C = set(range(2*N))
ans = []
q = [(C,0)]

while q:
    B,v = q.pop()
    #print(B,v)
    if len(B) == 2:
        B = sorted(list(B))
        ans.append(v^A[B[0]][B[1]-B[0]-1])
        continue
    s = min(B)
    for t in B-{s}:
        #print(s,t)
        q.append((B-{s,t}, v^A[s][t-s-1]))


print(max(ans))