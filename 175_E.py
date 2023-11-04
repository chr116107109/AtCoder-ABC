

R,C,K = map(int,input().split())

A = [[0 for j in range(C)] for i in range(R)]
for i in range(K):
    r,c,v = map(int,input().split())
    A[r-1][c-1] = v
before = [[0,0,0,0] for j in range(C+1)] 

for i in range(R):
    after = [[0,0,0,0] for j in range(C+1)]
    for j in range(C):
        after[j+1][0] = max(before[j+1])
        after[j+1][1] = max(after[j][1], after[j+1][0]+A[i][j])
        after[j+1][2] = max(after[j][2], after[j][1]+A[i][j])
        after[j+1][3] = max(after[j][3], after[j][2]+A[i][j])
        
    #print(before)
    #print(after)
    
    before = after[:]
        

print(max(after[-1]))