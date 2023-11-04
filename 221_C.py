
N = input()

ans = 0

for i in range(2**len(N)):
    A = ''
    B = ''
    for j in range(len(N)):
        if (i >> j) & 1:
            A += N[j]
        else:
            B += N[j]

    if A == '' or B == '':
        continue

    A = sorted(A,reverse = True)
    A = "".join(A)
    B = sorted(B,reverse = True)
    B = "".join(B)

    ans = max(ans,int(A)*int(B))

    #print(A)
    #print(B)

print(ans)
