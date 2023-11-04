
H,W = map(int,input().split())

A = [input() for i in range(H)]
B = [input() for i in range(H)]

ans = 'No'
for s in range(H):
    for t in range(W):
        same = True
        for i in range(H):
            for j in range(W):
                if A[i][j] == B[(i+s)%H][(j+t)%W]:
                    continue
                else:
                    same = False
                    break
        
        if same:
            #print(s,t)
            ans = 'Yes'
            break

print(ans)