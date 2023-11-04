

[S,T,X] = list(map(int,input().split()))

if T == 0:
    T = 24

if S < T :
    if S <= X and X < T:
        print('Yes')
    else:
        print('No')
else:
    if T <= X and X < S:
        print('No')
    else:
        print('Yes')
