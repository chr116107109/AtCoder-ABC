
[a,b] = list(map(int,input().split()))

if abs(a%10-b%10) == 1 or abs(a-b) == 1:
    print('Yes')
else:
    print('No')