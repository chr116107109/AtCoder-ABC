

T = int(input())
P = 998244353

def solve(N,S):
    max_rot_half = []
    M = N//2+N%2
    for i in range(M):
        max_rot_half.append(S[i])

    ans = 0
    #print(max_rot_half)
    #print(S[:N//2-1:-1])
    for i in range(M):
        ans += (ord(max_rot_half[i])-65) * pow(26,M-1-i,P)
        ans %= P

    if ''.join(max_rot_half[::-1]) <= S[N//2:]:
        ans += 1
    return ans%P

A = []
for i in range(T):
    N = int(input())
    S = input()
    A.append(solve(N,S))

for ans in A:
    print(ans)