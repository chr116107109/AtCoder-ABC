
N = int(input())
A = list(map(int,input().split()))


B = dict(zip(list(set(A)),[0]*len(set(A))))
for i in range(N):
    B[A[i]] += 1

A = sorted(list(set(A)))
for i in range(N):
    if A==[]:
        print(0)
        continue
    a = A.pop()
    print(B[a])
