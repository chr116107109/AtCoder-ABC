
[N,M] = list(map(int,input().split()))
S = list(map(str,input().split()))
T = list(map(str,input().split()))

nowS = 0
nowT = 0

for i in range(N):
    if T[nowT] == S[nowS]:
        print('Yes')
        nowT += 1
    else:
        print('No')


    nowS += 1 