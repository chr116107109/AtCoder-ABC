

N = int(input())
A = list(map(int,input().split()))
X = int(input())

sumA = sum(A)
n = X//sumA
x = X%sumA

#print(sumA)
#print(x,n)

a = 0
for i in range(N):
    a += A[i]
    if a > x:
        k = i + 1
        #print(k)
        break

print(N*n+k)
