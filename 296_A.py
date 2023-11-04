

N = int(input())
S = input()

T = ""
U = ""

for i in range(N):
    if i%2 == 0:
        T += "M"
        U += "F"
    else:
        T += "F"
        U += "M"

if S == T or S == U:
    print('Yes')
else:
    print('No')