
[N,X] = list(map(int,input().split()))
S = input()

M = 2**60 - 1

frag = 0
d = 0
for t in S:
    #print(X,d,t,frag)

    if frag == 0:
        if t == 'U':
            X = X//2
        elif t == 'R':
            X = 2*X + 1
        elif t == 'L':
            X = 2*X

        if X > M:
            frag = 1
            d = -1  
            continue
    
    if frag == 1:
        if t == 'U':
            d += 1
            if d == 0:
                X = X//2
                frag = 0
        else:
            d -= 1 


print(X)