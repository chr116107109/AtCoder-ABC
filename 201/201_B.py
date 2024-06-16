

N = int(input())

S = [input().split() for i in range(N)]

S.sort(key=lambda x:int(x[1]))
print(S[-2][0])
