
[N,Q] = list(map(int,input().split()))

d = [[i,0,0] for i in range(N)]

for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        d[q[1]-1][1] += q[2]
        d[q[2]-1][2] += q[1]
    if q[0] == 2:
        d[q[1]-1][1] = 0
        d[q[2]-1][2] = 0

    if q[0] == 3:
        ans_after = []
        ans_before = []

        now = q[1]

        while d[now-1][1] != 0:

        #for i in range(10**6):
        #    if d[now-1][1] == 0:
        #        break

            now = d[now-1][1]
            ans_after.append(now)

        now = q[1]

        #for i in range(10**6):
        while d[now-1][2] != 0:
            if d[now-1][2] == 0:
                break

            now = d[now-1][2]
            ans_before.append(now)

        ans_before = ans_before[::-1]


        ans = ans_before + [q[1]] + ans_after
        M = len(ans)
        ans = [M] + ans
        print(*ans)
