
N = int(input())

def factorization(n):
    arr = []
    if n == 1:
        return []
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

primes = factorization(N)

ans = 0

for [p,cnt] in primes:
    i = 1
    while cnt >= i:
        cnt -= i
        i += 1
    ans += i-1

print(ans)