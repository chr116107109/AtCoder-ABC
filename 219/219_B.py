
S1 = input()
S2 = input()
S3 = input()
T = list(map(int,input()))

S = ''
for i in range(len(T)):
    if T[i] == 1:
        S = S + S1
    if T[i] == 2:
        S = S + S2
    if T[i] == 3:
        S = S + S3

print(S)
