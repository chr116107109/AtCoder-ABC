

N = int(input())

ans = 0
for i in range(1,10**6+1):
    if int(str(i)*2) <= N:
        ans += 1

print(ans)