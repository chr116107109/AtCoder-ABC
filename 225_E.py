import sys
from decimal import Decimal

N = int(input())

xy = [list(map(int,input().split())) for i in range(N)]

eps = sys.float_info.min

def fraction(x,y):
    if y > 0:
        return x/y
    else:
        return 10**18


xy = sorted(xy,key = lambda x:fraction(x[1],x[0]-1))

tanxy_low = [(x[1]-1)/x[0] for x in xy]
tanxy_high = [fraction(x[1],x[0]-1) for x in xy]


ans = 0

high = 0

for i in range(N):

    if tanxy_low[i] < high:
        continue

    else:
        high = tanxy_high[i]
        ans += 1


print(ans)
