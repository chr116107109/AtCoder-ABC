
A,B,C = map(int,input().split())


if C%2 == 0:
    left = abs(A)
    right = abs(B)
else:
    left = A
    right = B

if left < right:
    print('<')
elif left > right:
    print('>')
else:
    print('=')


