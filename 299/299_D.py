

N = int(input())

l = 1
r = N-1

while l < r:
    #print(l,r)
    m = (l+r)//2
    print('? {}'.format(m+1))
    s = int(input())
    if s == 1:
        r = m
    else:
        l = m+1


print('! {}'.format(l))