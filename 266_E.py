
N = int(input())

p = [[0]*6 for i in range(N)]
p[0] = [1,2,3,4,5,6]
for i in range(1,N):

    for j in range(1,7):
        p[i][j-1] = max(j, sum(p[i-1])/6)

print(sum(p[-1])/6)