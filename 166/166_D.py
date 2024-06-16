
X = int(input())

C = {}

for i in range(-10**5,10**5):
    C[i**5] = i



for A in C:
    B = A - X
    if B in C:
        print(C[A],C[B])
        break