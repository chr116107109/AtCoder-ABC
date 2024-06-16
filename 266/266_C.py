
A = [list(map(int,input().split())) for i in range(4)]

ans = 'Yes'
for i in range(2):
    (x,y,z) = (A[i],A[(i+1)%4],A[(i+2)%4])
    (a,b,c) = (A[i+2],A[(i+3)%4],A[(i+4)%4])
    v = [x[0]-y[0],x[1]-y[1]]
    u = [z[0]-y[0],z[1]-y[1]]
    s = [a[0]-b[0],a[1]-b[1]]
    t = [c[0]-b[0],c[1]-b[1]]

    #print(x,y,z)
    #print(v,u)
    if (v[0]*u[1]-v[1]*u[0])*(s[0]*t[1]-s[1]*t[0]) < 0:
        ans = 'No'
        break

print(ans)