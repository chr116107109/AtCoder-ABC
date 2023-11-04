
N = int(input())
S = input()
W = list(map(int,input().split()))

W = [[W[i],int(S[i])] for i in range(N)]
W.sort(key=lambda x: x[0])

n_adlt = sum([w[1] for w in W])

ans = max(n_adlt,N-n_adlt)
X = n_adlt
prev = W[0][0]
for i in range(1,N):
    #print(X)
    
    if W[i-1][1] == 0:
        X += 1
    else:
        X -= 1
    if prev < W[i][0]:
        ans = max(X,ans)
        prev = W[i][0]

print(ans)
