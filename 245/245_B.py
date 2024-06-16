
N = int(input())
A = set(map(int,input().split()))

ans = 0
for i in range(1,2001):
    if ans in A:
        ans += 1

print(ans)

