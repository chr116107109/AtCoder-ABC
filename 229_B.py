
import sys

[A,B] = list(input().split())

keta = min([len(str(A)),len(str(B))])
A = list(reversed(A))
B = list(reversed(B))


for i in range(keta):
    if int(A[i]) + int(B[i]) < 10:
        continue
    else:
        print('Hard')
        sys.exit()

print('Easy')
