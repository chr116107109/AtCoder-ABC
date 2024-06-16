

N = int(input())

LA = [list(map(int,input().split())) for i in range(N)]

B = set()

for i in range(N):
    L = LA[i][0]
    
    B.add(str(LA[i][1:]))

print(len(B))
