

N,K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

left = 0
right = 10**12 + 10

while left < right:
    #print(left,right)
    m = (left+right)//2

    count = K
    for i in range(N):
        if A[i]*B[-i-1] > m:
            count -= -((m-A[i]*B[-i-1])//B[-i-1])
            #print(A[i],B[-1-i],count)
    if count < 0:
        left = m+1
    else:
        right = m

print(left)