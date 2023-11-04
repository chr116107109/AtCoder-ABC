

def is_black1(x,y,min,max,A,B):
    if x >= min + A and x <= max + A and y == (x-A) + B:
        return 'b'
    else:
        return 'w'

def is_black2(x,y,min,max,A,B):
    if  x >= min + A and x <= max + A and y == -(x-A) + B:
        return 'b'
    else:
        return 'w'



[N,A,B] = list(map(int,input().split()))

[P,Q,R,S] = list(map(int,input().split()))

mink1 = max(1-A,1-B)
maxk1 = min(N-A,N-B)

mink2 = max(1-A,B-N)
maxk2 = min(N-A,B-1)


for i in range(Q-P+1):
    ans = ''
    for j in range(S-R+1):
        x = P + i
        y = R + j
        if is_black1(x,y,mink1,maxk1,A,B) == 'b' or is_black2(x,y,mink2,maxk2,A,B) == 'b':
            ans += '#'
        else:
            ans += '.'

    print(ans)
