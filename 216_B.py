
N = int(input())
S = [input().split() for i in range(N)]
ans = 'No'
for i in range(N):
    for j in range(i+1,N):
        if S[i][0] == S[j][0] and S[i][1] == S[j][1]:
            ans = 'Yes'

print(ans)