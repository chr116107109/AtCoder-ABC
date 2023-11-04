
N = int(input())
S = [input() for i in range(N)]

frag = 0
for i in range(N):
    for j in range(N):
        #print(i,j)
        if i + 6 <= N:
           T = [S[i][j],S[i+1][j],S[i+2][j],S[i+3][j],S[i+4][j],S[i+5][j]] 
           #print(T)
           if T.count('.') <= 2:
               frag = 1
               break
        if j + 6 <= N:
            T = [S[i][j],S[i][j+1],S[i][j+2],S[i][j+3],S[i][j+4],S[i][j+5]] 
            #print(T)
            if T.count('.') <= 2:
               frag = 1
               break
               
        if i + 6 <= N and j + 6 <= N :
            T = [S[i][j],S[i+1][j+1],S[i+2][j+2],S[i+3][j+3],S[i+4][j+4],S[i+5][j+5]]
            #print(T)
            if T.count('.') <= 2:
               frag = 1
               break

        if i + 6 <= N and j - 5 >= 0 :
            T = [S[i][j],S[i+1][j-1],S[i+2][j-2],S[i+3][j-3],S[i+4][j-4],S[i+5][j-5]]
            #print(T)
            if T.count('.') <= 2:
               frag = 1
               break


if frag == 0 :
    print('No')
else:
    print('Yes')
