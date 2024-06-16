

[N,X] = list(map(int,input().split()))

A = list(map(int,input().split()))

def is_ok(Y,A,N,ans):
    ans = 0
    frag = 0
    for i in range(N):
        if Y < A[N-1-i]:
            break
        b = Y//A[N-1-i]
        ans += b
        Y -= b*A[N-1-i]
    if Y == 0:
        return True
    else:
        return False

for i in range(N+1):
    ans = 0
    Y = X + sum(A[0:i])
    print(Y)
    if is_ok(Y,A,N,ans):
        print(ans)
        break
