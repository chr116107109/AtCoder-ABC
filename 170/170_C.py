
X,N = map(int,input().split())
A = set(map(int,input().split()))


ans = -101
for x in range(X-101,X+102):
    if not x in A:
        if abs(X-x) < abs(X-ans):
            ans = x

print(ans)