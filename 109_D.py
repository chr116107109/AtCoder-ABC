
H,W = map(int,input().split())

A = [list(map(int,input().split())) for i in range(H)]

q = []
for i in range(H):
    for j in range(W):
        if A[i][j]%2 == 1:
            q.append([i+1,j+1])

M = len(q)

ans = []
for i in range(M//2):

    s = q[2*i]
    t = q[2*i+1]

    for j in range(abs(s[0]-t[0])):
        if s[0] < t[0]:
            ans.append([s[0]+j,s[1],s[0]+j+1,s[1]])
        else:
            ans.append([s[0]-j,s[1],s[0]-j-1,s[1]])
    for j in range(abs(s[1]-t[1])):
        if s[1] < t[1]:
            ans.append([t[0],s[1]+j,t[0],s[1]+j+1])
        else:
            ans.append([t[0],s[1]-j,t[0],s[1]-j-1])



print(len(ans))
for a in ans:
    print(*a)