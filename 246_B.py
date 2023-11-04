import math

A,B = map(int,input().split())

print(A/math.sqrt(A**2+B**2),B/math.sqrt(A**2+B**2))