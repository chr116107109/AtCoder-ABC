
N,K = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    A[i] = [A[i],i]

from collections import deque

A.sort(key = lambda x:x[0])
get_in_one_cycle = len([a for a in A if a[0]>0])
A = deque(A)
be_zero = set()
while A and A[0][0] == 0:
    be_zero.add(A[0][1])
    A.popleft()

sum_cycle = 0

while A:
    #print(A)
    n_cycle = A.popleft()
    #print(n_cycle,sum_cycle)
    #print(K)
    if K > (n_cycle[0]-sum_cycle)*(len(A)+1):
        K -= (n_cycle[0]-sum_cycle)*(len(A)+1)
        sum_cycle += n_cycle[0] - sum_cycle
    else:
        sum_cycle += K//(len(A)+1)
        K = K%(len(A)+1)
        A.append(n_cycle)
        break

ans = [0] * N
#print(A,K)
for a in A:
    ans[a[1]] = a[0] - sum_cycle
if K > 0:
    A = sorted(list(A),key = lambda x: x[1])
    for a in A:
        ans[a[1]] -= 1
        K -= 1
        if K == 0:
            break

print(*ans)