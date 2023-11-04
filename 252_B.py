
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

kirai = set()

for i in range(K):
    kirai.add(A[B[i]-1])

if max(A) in kirai:
    print('Yes')
else:
    print('No')
