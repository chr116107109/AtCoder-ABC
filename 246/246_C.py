import sys

N,K,X = map(int,input().split())
A = list(map(int,input().split()))

#A = sorted(A, key = lambda y: (y//X==0)*(y//X) + (1-(y%X==0))*(X-y%X))

#A = sorted(A,reverse=True)
ans = sum(A)

for i in range(N):
    #print(ans,K)
    
        #ans -= X*min(A[i]//X,K)
    j = min(A[i]//X,K)
    K -= j
    A[i] -= X*j
    
    if K == 0:
        break

else:
    A.sort()
    while K > 0 and A:
        A.pop()
        K -= 1
        

print(sum(A))
