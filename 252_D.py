
from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

def naive(A):
    N = len(A)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if A[i] != A[j] and A[i] != A[k] and A[j] != A[k]:
                    count += 1
    
    return count

N = int(input())
A = list(map(int,input().split()))

d = dict()
ans = 0
kaburi = 0 
for i in range(N):

    if A[i] in d:
        if i-d[A[i]] >= 2:
            if d[A[i]] >= 2:
                ans += combinations_count(i - d[A[i]],2) - kaburi + combinations_count(d[A[i]],2)
            else:
                ans += combinations_count(i - d[A[i]],2) - kaburi

        d[A[i]] += 1
        if d[A[i]] == 2:
            kaburi += 1
        elif d[A[i]] > 2:
            kaburi += -combinations_count(d[A[i]]-1,2)+combinations_count(d[A[i]],2)
    else:
        if len(d) >= 2:
            ans += combinations_count(i, 2) - kaburi
        d[A[i]] = 1
    
    #print(d)
print(ans)
    #print(naive(A[:i+1]))

        