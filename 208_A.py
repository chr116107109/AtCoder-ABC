

x = list(map(int, input().split()))
A = x[0]
B = x[1]

if B > 6*A or B < A:
    print("No")
else:
    print("Yes")
