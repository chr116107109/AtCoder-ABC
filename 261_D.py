

N,M = map(int,input().split())
X = list(map(int,input().split()))
CY = [list(map(int,input().split())) for i in range(M)]

c_dict = {c:y for [c,y] in CY}

d = [[0]*(N+1) for i in range(N+1)]

for i in range(1,N+1):
    d[i][0] = max([d[i-1][j] for j in range(N+1)]) 
    for j in range(1,i+1):
        d[i][j] = d[i-1][j-1] + X[i-1]
        if j in c_dict:
            d[i][j] += c_dict[j]
    
    #print(d)

print(max([d[N][j] for j in range(N+1)]))