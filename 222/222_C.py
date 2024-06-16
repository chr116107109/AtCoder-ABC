

def janken(a,b):
    if a == b:
        return 'draw'
    elif a == 'G' and b == 'C':
        return 'left'
    elif a == 'C' and b == 'P':
        return 'left'
    elif a == 'P' and b == 'G':
        return 'left'
    elif a == 'C' and b == 'G':
        return 'right'
    elif a == 'P' and b == 'C':
        return 'right'
    elif a == 'G' and b == 'P':
        return 'right'



[N,M] = list(map(int,input().split()))
A = [input() for i in range(2*N)]


JT = [[i,0] for i in range(2*N)]

for i in range(M):
    for j in range(N):

        if janken(A[JT[2*j][0]][i],A[JT[2*j+1][0]][i]) == 'draw':
        #    print('{}vs{} draw'.format(JT[2*j],JT[2*j+1]))
            continue
        elif janken(A[JT[2*j][0]][i],A[JT[2*j+1][0]][i]) == 'right':
        #    print('{}vs{} right win'.format(JT[2*j],JT[2*j+1]))
            JT[2*j+1][1] += 1
        elif janken(A[JT[2*j][0]][i],A[JT[2*j+1][0]][i]) == 'left':
        #    print('{}vs{} left win'.format(JT[2*j],JT[2*j+1]))
            JT[2*j][1] += 1

    JT = sorted(JT, reverse = True,key=lambda x: 1000*x[1] - x[0])
    #print(JT)

    #for k in range(j+2,-1,-1):
    #    m = [l for l in JT if l[1] == k]
    #    m = sorted(m , key=lambda x: x[0])
    #    #print(m)
    #    if not m == []:
    #        ans.extend(m)

    #JT = ans

    #print(JT)


for i in range(2*N):
    print(JT[i][0]+1)
