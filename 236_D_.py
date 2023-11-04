
N = int(input())
A = [list(map(int,input().split())) for i in range(2*N-1)]

import itertools

def f(B,score):
    if B == []:
        return score
    
    ans = 0
    i = B[0]
    for j in B[1:]:
        B_copy = B[:]
        B_copy.remove(i)
        B_copy.remove(j)
        ans = max(f(B_copy, score^A[i][j-i-1]),ans)

    return ans

B = list(range(2*N))
score = 0
print(f(B,score))