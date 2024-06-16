

L,N,M = map(int,input().split())

d = []

now = 1
for i in range(N):
    v,l = map(int,input().split())
    d.append([now,v,'a','l'])
    d.append([now+l-1,v,'a','r'])
    now += l
now = 1
for i in range(M):
    v,l = map(int,input().split())
    d.append([now,v,'b','l'])
    d.append([now+l-1,v,'b','r'])
    now += l


a = [0,-1]
b = [0,-1]

d.sort(key=lambda x:x[0])

ans = 0
for i in range(2*(N+M)):
    s = d[i]

    if s[3] == 'l':
        if s[2] == 'a':
            a[0] = s[0]
            a[1] = s[1]
        if s[2] == 'b':
            b[0] = s[0]
            b[1] = s[1]

    if s[3] == 'r':
        if s[2] == 'a':
            if a[1] == b[1]:
                ans += s[0] - max(a[0],b[0]) + 1
                a[1] = -1
        if s[2] == 'b':
            if a[1] == b[1]:
                ans += s[0] - max(a[0],b[0]) + 1
                b[1] = -1
    #print(s)
    #print('a',a)
    #print('b',b)
    #print(ans)
print(ans)
    


    