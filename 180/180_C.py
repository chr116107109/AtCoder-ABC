

N = int(input())

M = int(N**(0.5))

ans = set()
for i in range(1,M+1):
    if N%i == 0:
        ans.add(i)
        ans.add(N//i)

ans = list(ans)
ans.sort()
print(*ans, sep='\n')