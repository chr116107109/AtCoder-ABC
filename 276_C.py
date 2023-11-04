
N = int(input())
P = list(map(int,input().split()))

import math
import itertools

def naive(N):
    d = []
    for p in itertools.permutations(range(1,N+1)):

        d.append(p)
    d.sort()

    for i,s in enumerate(d):
        print(i,s)

def list_rank(A):
    d = {}
    B = sorted(A)
    for i,a in enumerate(B):
        d[a] = i+1

    return d
    

def rank(N,P):
    rank = 0
    for i,p in enumerate(P):
        d = list_rank(P[i:])
        rank += (d[p]-1)*math.perm(N-i-1)

    return rank

def ranktoList(N,rank):
    d = list(range(1,N+1))
    r = 0
    ans = []
    for i in range(N):
        j = 0
        while r+math.perm(N-i-1) <= rank:
    
            r += math.perm(N-i-1)
            j += 1
        #print(r,j)
        ans.append(d[j])
        d.remove(ans[-1])

    return ans

r = rank(N,P)
print(*ranktoList(N,r-1))