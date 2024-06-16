

H,W,N,h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
comm = [[{} for j in range(W+1)] for i in range(H+1)]
import copy
def union_dic(b,d2):
    for a in d2:
        if a in b:
            b[a] += d2[a]
        else:
            b[a] = d2[a]

def diff_dic(b,d2):
    for a in d2:
        if a in b:
            b[a] -= d2[a]

for i in range(1,H+1):
    for j in range(1,W+1):
        union_dic(comm[i][j],comm[i][j-1])
        union_dic(comm[i][j],comm[i-1][j])
        diff_dic(comm[i][j],comm[i-1][j-1])
        if A[i-1][j-1] in comm[i][j]:
            comm[i][j][A[i-1][j-1]] += 1
        else:
            comm[i][j][A[i-1][j-1]] = 1
    


for i in range(H-h+1):
    q = []
    ans = copy.deepcopy(comm[H][W])
    diff_dic(ans,comm[i+h][w])
    union_dic(ans,comm[i][w])
    

    for j in range(W-w+1):
        count = 0
        for a in ans:
            if ans[a] > 0:
                count += 1
        q.append(count)
        #print(ans)
        if j == W-w:
            break
        for k in range(h):
            if A[i+k][j+w] in ans:
                ans[A[i+k][j+w]] -= 1
            if A[i+k][j] in ans:
                ans[A[i+k][j]] += 1
            else:
                ans[A[i+k][j]] = 1
        
    print(*q)
        