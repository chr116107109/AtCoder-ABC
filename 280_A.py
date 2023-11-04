
H,W = map(int,input().split())

ans = 0
for i in range(H):
    S = input()
    ans += len([s for s in S if s == '#'])

print(ans)