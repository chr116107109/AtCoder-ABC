
X = input()
M = int(input())

left = 1
right = M+1

while left < right:
    m = (left+right)//2
    #print(m)
    Y = 0
    for i in range(len(X)):
        Y += int(X[len(X)-1-i])*(m**i)

    if m <= int(max(X)) or Y <= M:
        left = m + 1
    else:
        right = m

if len(X) == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
else:
    print(max(left - int(max(X)) - 1, 0))
