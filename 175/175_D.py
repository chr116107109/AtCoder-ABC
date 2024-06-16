
N,K_ori = map(int,input().split())

P = list(map(int,input().split()))
C = list(map(int,input().split()))
for i in range(N):
    P[i] -= 1

score = []
for i in range(N):
    now = i
    K = K_ori
    before_loop = set()
    while not now in before_loop:
        now = P[now]
        before_loop.add(now)

    loop = set()
    while not now in loop:
        loop.add(now)
        now = P[now]
    
    last_ind = now
    #score = []
    ans = 0
    if K < len(before_loop):
        now = i
        for j in range(K):
            now = P[now]
            ans += C[now]
            score.append(ans)
        
    else:
        now = i
        for j in range(len(before_loop)):
            now = P[now]
            ans += C[now]
            score.append(ans)
        K -= len(before_loop)
        scoreInLoop = sum(C[j] for j in loop)
        if scoreInLoop < 0:
            for j in range(min(len(loop), K)):
                now = P[now]
                ans += C[now]
                score.append(ans)
        else:
            ans += (K//len(loop))*scoreInLoop
            K %= len(loop)
            score.append(ans)
            for j in range(min(len(loop),K)):
                now = P[now]
                ans += C[now]
                score.append(ans)
        
        
print(max(score))



