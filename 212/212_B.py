
X = str(input())

X1 = int(X[0])
X2 = int(X[1])
X3 = int(X[2])
X4 = int(X[3])

#print(X1,X2,X3,X4)
a = 0;

if X1==X2 and X2==X3 and X3==X4:
    a=1
    print('Weak')

if (X1+1)%10 == X2%10 and (X2+1)%10 == (X3)%10 and (X3+1)%10 == (X4)%10:
    a=1
    print('Weak')

if a == 0:
    print('Strong')
