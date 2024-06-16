
N,T = map(int,input().split())

C = list(map(int,input().split()))
R = list(map(int,input().split()))

if T in C:
    ind = []
    ans = 0
    now = 0
    for i in range(N):
        if C[i] == T and R[i] > now:
            ans = i
            now = R[i]
else:
    T = C[0]
    ind = []
    ans = 0
    now = 0
    for i in range(N):
        if C[i] == T and R[i] > now:
            ans = i
            now = R[i]

print(ans+1)