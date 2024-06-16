
A,B,C,D,E,F,X = map(int,input().split())

takahashi = (X//(A+C))*B*A
if X%(A+C) >= A:
    takahashi += A*B
else:
    takahashi += (X%(A+C))*B 

aoki = (X//(D+F))*E*D
if X%(D+F) >= D:
    aoki += D*E
else:
    aoki += (X%(D+F))*E

if takahashi > aoki :
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')

