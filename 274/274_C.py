
N = int(input())
A = list(map(int,input().split()))

parent = [-1] * (2*N+1)
parent[0] = 0
sedai = [0] * (2*N+1)

for i in range(1,N+1):
    parent[2*i-1] = A[i-1]-1
    parent[2*i] = A[i-1]-1
    sedai[2*i-1] = sedai[A[i-1]-1] + 1
    sedai[2*i] = sedai[A[i-1]-1] + 1

for i in range(2*N+1):
    print(sedai[i])