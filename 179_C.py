

N = int(input())


ans = 0
s = set()
for a in range(1,N+1):
    b = a
    while a*b < N:
        ans += 1
        if a != b:
            ans += 1
        b += 1
        

print(ans)