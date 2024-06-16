

N = int(input())

d = [[0]*10 for i in range(10)]
for i in range(1,N+1):
    s = str(i)
    d[int(s[0])][int(s[-1])] += 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        ans += d[i][j] * d[j][i]

print(ans)