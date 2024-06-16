
import math
N = int(input())
x,y = map(int,input().split())
s,t = map(int,input().split())

theta = (N-2)*math.pi/N/2
X = ((s-x)**2+(t-y)**2)**0.5
R = (math.sin(2*math.pi/N)*X/2/math.sin(theta))/X
print(x+((s-x)*math.cos(theta)+(t-y)*math.sin(theta))*R,y+(-(s-x)*math.sin(theta)+(t-y)*math.cos(theta))*R)