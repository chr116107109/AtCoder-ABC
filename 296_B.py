

S = [input() for i in range(8)]


for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            ans = chr(97+j) +str(8-i)
            print(ans)