
N,M = map(int,input().split())
S = []
for i in range(M):
    res = list(map(int,input().split()))
    s = res[1:]
    S.append(s)

P = list(map(int,input().split()))

ans = 0
for i in range(2**N):
    ok = True
    for j in range(M):
        count = 0
        for s in S[j]:
            if i & (1<<(s-1)) != 0:
                count += 1
        
        if P[j] != count%2:
            ok = False

    if ok:
        ans += 1
            

print(ans)