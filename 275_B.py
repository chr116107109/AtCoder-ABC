
A,B,C,D,E,F = map(int,input().split())

P = 998244353

X = 1
X = (X*A)%P
X = (X*B)%P
X = (X*C)%P
Y = 1
Y = (Y*D)%P
Y = (Y*E)%P
Y = (Y*F)%P

print((X-Y)%P)

