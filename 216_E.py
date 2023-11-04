
N,K = map(int,input().split())
A = list(map(int,input().split()))
A.append(0)
A.sort()


num = 1
ans = 0
while len(A)>1 and K > 0 :
    a = A.pop()
    b = A[-1]
    if a == b:
        num += 1
        continue
    #print(K,a,b)
    if (a-b)*num <= K:
        K -= (a-b)*num
        ans += ((a+b+1)*(a-b)*num)//2
        num += 1
    else:
        c = a - K//num
        K -= (a-c)*num
        ans += ((a+c+1)*(a-c)*num)//2
        ans += c*K
        K = 0
    #print(ans)
print(ans)