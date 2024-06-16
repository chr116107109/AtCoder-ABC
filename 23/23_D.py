

N = int(input())

H = [0] * N
S = [0] * N

MAX = 0
for i in range(N):
    [H[i],S[i]] = list(map(int, input().split()))
    MAX = max(MAX,H[i]+S[i]*N)


M = MAX//2

for i in range(50):

    #print('M is {}'.format(M))
    SMALL_THAN_M = 1
    L = 0
    s = [0] * N
    for j in range(N):
        #print('{} step'.format((M - H[j])//S[j]+1 ))
        s[j] = (M - H[j])//S[j]+1

    s = sorted(s)
    #print(*s)

    for j in range(N):
        if s[j] >= j+1:
            continue
        else:
            SMALL_THAN_M = 0
            break

    if SMALL_THAN_M == 1:
        #print('smaller then M')
        M = M - MAX/(2**(i+2))
    else:
        #print('larger then M')
        M = M + MAX/(2**(i+2))

print(round(M))
