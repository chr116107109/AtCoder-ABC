
K = int(input())
A,B = map(int,input().split())

if A//K < B//K or A%K == 0 or B%K==0:
    print('OK')
else:
    print('NG') 