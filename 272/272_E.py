
N,M = map(int,input().split())
A = list(map(int,input().split()))

d = [set() for i in range(M+1)] #d[index] = {possible value}

for i in range(N):
    num = i+1
    ind = 0
    B = A[i]
    if A[i] < 0:
        ind = -A[i]//num
        B += num*ind
    #print(B,ind,num)
    while B <= N and ind <= M:
        if B >= 0:
            d[ind].add(B)
        B += num
        ind += 1
    #print(d)

for i in range(1,M+1):
    k = 0 
    while k in d[i]:
        k+=1
    print(k)