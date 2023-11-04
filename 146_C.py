

A,B, X = map(int,input().split())

left = 0
right = 10**9+10

while left < right:
    m = (left+right)//2

    d = len(str(m))
    if A*m+B*d <= X:
        left = m+1
    else:
        right = m

print(max(min(left-1,10**9),0))