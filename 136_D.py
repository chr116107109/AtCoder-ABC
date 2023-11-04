
N = int(input())

if N%2 == 1:
    print(0)
else:
    N //= 2
    ans = 0
    i = 1
    while N >= pow(5,i):
        ans += N//pow(5,i)
        i += 1
    
    print(ans)