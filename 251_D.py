
import itertools

W = int(input())

N = 300
A = list(range(1,100)) + [i*100 for i in range(1,100)] + [j*10000 for j in range(1,101)]

print(len(A))
print(*A)