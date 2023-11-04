

N = int(input())

left = 0
right = N-1
while left < right:
    m = (left + right)//2
    print('? {} {} {} {}'.format(left+1,m+1,1,N))
    T = int(input())
    if T < (m+1-left):
        right = m
    else:
        left = m + 1
X = left


left = 0
right = N-1
while left < right:
    m = (left + right)//2
    print('? {} {} {} {}'.format(1,N,left+1,m+1))
    T = int(input())
    if T < (m+1-left):
        right = m
    else:
        left = m + 1

Y = left

print('! {} {}'.format(X+1,Y+1))