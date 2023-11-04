
X,Y,A,B,C = map(int,input().split())

import itertools

L = [A,B,C]
ans = 'No'
for i in range(3):
    a = L[i]
    b,c = L[(i+1)%3], L[(i+2)%3]

    for i in range(1,int(a**(1/2))+1):
        if i <= X and -(-a//i) <= Y:
            S = (X-i)*(-(-a//i))
            T = X*(Y+(-a//i))
            if b <= S and c <= T or b <= T and c <= S:
                ans = 'Yes'
                print(a,i)
                break
            S = (X-i)*Y
            T = i*(Y+(-a//i))
            if b <= S and c <= T or b <= T and c <= S:
                ans = 'Yes'
                print(a,i)
                break
            

print(ans)