
N,M = map(int,input().split())
A = list(map(int,input().split()))
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

p = set()
for i in range(N):
    if A[i] == 1:
        continue
    arr = factorization(A[i])
    for a in arr:
        p.add(a[0])

ans = [1]
for i in range(2,M+1):
    flag = 0
    for a in p:
        if i % a == 0:
            flag = 1
            break
    if flag == 0:
        ans.append(i)


print(len(ans))
for a in ans:
    print(a)