
[X,Y] = list(map(int,input().split()))

ans = 0
for i in range(10000):
    if X >= Y:
        print(ans)
        break
    else:
        ans += 1
        X += 10
