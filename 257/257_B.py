
N,K,Q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))

for l in L:
    #print(A)
    if A[l-1] == N:
        continue
    else:
        if l == K:
            A[l-1] += 1
        elif A[l-1] + 1 == A[l]:
            continue
        else:
            A[l-1] += 1

print(*A)