
S = input()

def num(s):
    return ord(s)-65

ans = 0
N = len(S)
ans += sum([26**i for i in range(1,N)])

for i in range(N):
    ans += num(S[i])*(26**(N-i-1))

print(ans+1)