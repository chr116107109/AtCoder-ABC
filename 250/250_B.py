
N,A,B = map(int,input().split())
s = ''
for i in range(A*N):
    s = ''
    for j in range(B*N):

        if ((i//A) + (j//B))%2 ==0:
            s += '.'
        else:
            s += '#'
    
    print(s)

