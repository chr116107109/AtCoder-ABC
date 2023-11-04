N = int(input())

S = [[input(), i] for i in range(N)]
S.sort()

ans = [0] * N
for i in range(N):
    if i == N-1:
        [s,si],[t,ti] = S[i],S[i-1]
    else:
        [s,si],[t,ti] = S[i],S[i+1]

    m = min(len(s),len(t))
    count = 0
    for j in range(m):
        if s[j] == t[j]:
            count += 1
        else:
            break
    ans[si] = count

    if i > 0:
        [t,ti] = S[i-1]
        m = min(len(s),len(t))
        count = 0
        for j in range(m):
            if s[j] == t[j]:
                count += 1
            else:
                break
        ans[si] = max(ans[si],count)

    #print(i,ans)

for i in range(N):
    print(ans[i])

