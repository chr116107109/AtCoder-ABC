
H,W = map(int,input().split())
S = [input() for i in range(H)]

mikke = [-1, -1]
for i in range(H):

    for j in range(W):
        if S[i][j] == 'o':
            if mikke == [-1,-1]:
                mikke = [i,j]
            else:
                print(abs(mikke[0]-i)+abs(mikke[1]-j))

