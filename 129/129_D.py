
H,W = map(int,input().split())
S = [input() for i in range(H)]

def calc_d(s):
    now = s[:]
    d = 0
    while now[0] < H and S[now[0]][now[1]] != '#':
        d += 1
        now[0] += 1
    return d
def calc_l(s):
    now = s[:]
    l = 0
    while now[1] < W and S[now[0]][now[1]] != '#':
        l += 1
        now[1] += 1
    return l

ans = 0
L = [[0]*W for i in range(H)]
D = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            continue

        if j == 0 or (j>0 and S[i][j-1]=='#'):
            l = calc_l([i,j])
        else:
            l = L[i][j-1]
        if i == 0 or (i>0 and S[i-1][j]=='#'):
            d = calc_d([i,j])
        else:
            d = D[i-1][j]
        
        L[i][j] = l
        D[i][j] = d

        ans = max(ans,l+d-1)

print(ans)