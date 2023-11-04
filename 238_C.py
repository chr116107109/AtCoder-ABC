
N = int(input())

T = 998244353
for i in range(19):
    if N < 10**i:
        keta = i
        break

ans = 0
for i in range(keta-1):
    if i == 0:
        ans += 45
    else:
        ans += (((1 + (10**(i+1)- 10**i)) * (10**(i+1)-10**i)) // 2 ) % T
        ans = ans % T


    #print(ans)

ans += ((1 + (N - 10**(keta-1) + 1)) *  (N - 10**(keta-1) + 1) // 2 ) % T
ans = ans % T

print(ans)