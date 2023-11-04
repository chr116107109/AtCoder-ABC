

N = int(input())
D = []
for i in range(N):
    L,R = map(int,input().split())
    D.append([L,'l'])
    D.append([R,'r'])

D.sort(key = lambda x:100*x[0]+ord(x[1]))

#print(D)
num_L = 0
num_R = 0
for i in range(2*N):
    if num_L == num_R :
        left = D[i][0]
    
    if num_L - num_R == 1 and D[i][1] == 'r':
        print(left,D[i][0])
        
    if D[i][1] == 'r':
        num_R += 1
    elif D[i][1] == 'l':
        num_L += 1
