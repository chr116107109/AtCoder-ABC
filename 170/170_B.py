

X,Y = map(int,input().split())

ans = 'No'
for i in range(100):
    for j in range(100):
        if 2*i+j*4 == Y and i+j == X:
            ans = 'Yes'

print(ans)