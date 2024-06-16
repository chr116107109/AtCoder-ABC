

N,M = map(int,input().split())

poles = []
color_num = [[0, []] for i in range(N)]
cantake = []

def post_color(p,cantake,color_num,n):
    color_num[p[-1]-1][0] += 1
    color_num[p[-1]-1][1].append(n)
    if color_num[p[-1]-1][0] == 2:
        cantake.append(color_num[p[-1]-1][1])
    #print(color_num)

for i in range(M):
    k = int(input())
    p = list(map(int,input().split()))
    poles.append(p)
    post_color(p,cantake,color_num,i)

while cantake:
    #print(cantake)
    [i,j] = cantake.pop()
    poles[i].pop()
    poles[j].pop()

    p = poles[i]
    if p:
        post_color(p,cantake,color_num,i)
    p = poles[j]
    if p:
        post_color(p,cantake,color_num,j)

    N -= 1

if N > 0:
    print('No')
else:
    print('Yes')