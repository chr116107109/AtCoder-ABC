
S = input().split()
T = input().split()

if T == [S[0],S[1],S[2]] or T == [S[1],S[2],S[0]] or T == [S[2],S[0],S[1]]:
    print('Yes')
else:
    print('No')
