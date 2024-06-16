
N,K = map(int,input().split())

S = input()

T = ''
for i in range(N):
    if S[i] == 'o' and K > 0:
        T += 'o'
        K -= 1
    else:
        T += 'x'

print(T)