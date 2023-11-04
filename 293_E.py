

A,X,M = map(int,input().split())

def solve(l,r):

    if l == r:
        return pow(A,l,M)
    
    m = (l+r)//2

    left = solve(l,m)

    if (r-l)%2 == 1:
        return (left + left*pow(A,m-l+1,M))%M
    else:
        return (left + left*pow(A,m-l+1,M) - pow(A,r+1,M))%M
    
ans = solve(0,X-1)

print(ans)