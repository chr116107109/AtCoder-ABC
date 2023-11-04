

from os import sep


N,X,Y = map(int,input().split())
A = list(map(int,input().split()))

def separate(A):
    B = [[]]
    for i in range(N):
        if A[i] < Y or A[i] > X:
            if B[-1] != []:
                B.append([])
        else:
            B[-1].append(A[i])

    return B

def solve(B):
    i, j, countX, countY, res = 0, 0, 0, 0, 0
    while i != len(B):
        while j != len(B) and (countX == 0 or countY == 0):
            if B[j] == X:
                countX += 1
            if B[j] == Y:
                countY += 1
            j += 1
        if countX > 0 and countY > 0:
            res += len(B) + 1 - j
        if B[i] == X:
            countX -= 1
        if B[i] == Y:
            countY -= 1
        i += 1
    return res


B = separate(A)

ans = 0
for a in B:
    ans += solve(a)


print(ans)