

R,X,Y = map(int,input().split())

r = X**2 + Y**2
import math

if r == R**2:
    print(1)
elif math.sqrt(r) <= 2*R:
    print(2)
else:
    print(math.ceil(math.sqrt(r)/R))