

[A,B] = list(map(int, input().split()))

#print(A,B)
if A>0 and B==0:
    print('Gold')
if A>0 and B>0:
    print('Alloy')
if A==0 and B>0:
    print('Silver')
