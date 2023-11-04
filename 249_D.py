
N = int(input())
A = list(map(int,input().split()))

Max = max(A)
Alist = [0] * (10**6)

for i in range(N):
    Alist[A[i]] += 1

j = 1
ans = 0
yakusu = []    


while j <= Max**(1/2):
    if Alist[j]>0:
    
        ans += Alist[j]*Alist[j]*Alist[j*j]
        for i in range(j+1,Max+1):
            if i * j < Max+1:
                ans += (Alist[j]*Alist[i]*Alist[i*j])*2
            #print(j,i,ans)
    
    j += 1



print(ans)
        



