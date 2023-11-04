
import itertools
import sys

N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

now = {A[0],B[0]}
if N == 1:
    print('Yes')
    sys.exit()
for i in range(1,N):
    ans = 'No'
    next = set()
    for k,l in itertools.product(now,[A[i],B[i]]):
        if abs(l-k) <= K:
            ans = 'Yes'
            next.add(l)
    if ans == 'No':
        break
    now = next
    if not now:
        break
print(ans)