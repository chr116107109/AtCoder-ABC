
from re import M


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr


K = int(input())
A = factorization(K)

left = 0
right = 10**20

while left < right:
    m = (left+right)//2
    ok = True
    #print(m)
    for a in A:
        p = a[0]
        n = a[1]
        q = p
        n_p = 0
        while m//q > 0:
            n_p += m//q
            q *= p
        #print(p,n_p,n)
        if n_p < n:
            ok = False
            break
    if ok:
        right = m
    else:
        left = m+1

print(right)