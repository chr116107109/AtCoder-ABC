

[N,W] = list(map(int, input().split()))

AB = [list(map(int,input().split())) for i in range(N)]

AB = sorted(AB, key = lambda x: x[0], reverse = True)

now = 0
ans = 0
for i in range(N):
    if (W - now) > AB[i][1]:
        ans += AB[i][0] * AB[i][1]
        now += AB[i][1]

    else:
        ans += AB[i][0] * (W - now)
        break


print(ans)
