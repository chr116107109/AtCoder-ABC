
xy = list(map(int,input().split()))

x = [xy[0],xy[1]]
y = [xy[2],xy[3]]



def dist(x,y):
   return ((x[0]-y[0])**2 + (x[1]-y[1])**2)

frag = 0
for i in range(-10,10):
    for j in range(-10,10):
        z = [x[0]+i,x[1]+j]
        #print(z)
        #print(dist(x,z))

        if dist(x,z) == 5 and dist(y,z) == 5:
            frag = 1


if frag == 1:
    print('Yes')
else:
    print('No')
