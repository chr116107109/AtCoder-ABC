
S = [input() for i in range(10)]

A = 1
B = 10

for i in range(9):
    if S[i] == '.' * 10 and '#' in S[i+1]:
        A = i+2
    if S[i+1] == '.' * 10 and '#' in S[i]:
        B = i+1

C = 1
D = 10

for i in range(9):
    if S[A-1][i] == '.' and S[A-1][i+1] == '#':
        C = i+2
    if S[A-1][i+1] == '.' and S[A-1][i] == '#':
        D = i+1
    

print(A,B)
print(C,D)