
N = int(input())
T = input()

now = 0
ans = -1
while now < N:

    if T[now] == T[-1]:
        l = 1
        while T[now+l] == T[-1-l] and l <= N-now+1:
            l += 1
        
        if l == N-now:
            if T[:now] == T[N+now:N:-1]:
                ans = [T[now:now+N], now]
                break
    now += 1
print(ans)