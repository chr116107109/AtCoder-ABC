
N = int(input())
S = input()

l = 0
r = N
if not 'o' in S or not '-' in S:
    print(-1)
else:
    ans = 0
    l = 0
    for i in range(N):
        if S[i] == 'o':
            l += 1
        else:
            l = 0
        ans = max(ans,l)
    print(ans)