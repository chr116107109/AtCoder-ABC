

S = input()

K = int(input())

N = len(S)

ruiseki = [0] * (N+1)
M = 0
for i in range(N):
    if S[i] == '.':
        ruiseki[i+1] = ruiseki[i] + 1
    else:
        ruiseki[i+1] = ruiseki[i]


def is_ok(N,M,K,ruiseki):
    if M <= K:
        possible = 1
    elif M == N:
        possible = 0
        if ruiseki[N-1] <= K:
            possible = 1
    elif M > N:
        possible = 0

    else:
        possible = 0
        for j in range(N - M + 1):
            if ruiseki[j+M] - ruiseki[j] <= K:
                possible = 1
                break

    if possible == 1:
        return True | False



start = 0
end = N + 1
for i in range(30):
    M = (start + end) // 2
    #print([start, M , end])
    if is_ok(N,M,K,ruiseki):
        start = M
        #print('larger')
    else:
        end = M
        #print('smaller')

    #print(M)
    #print(intM)

if start+1 <= N and is_ok(N,start+1,K,ruiseki):
    ans = start + 1
else:
    ans = start

print(ans)
