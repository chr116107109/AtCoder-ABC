
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

X,K = map(int,input().split())
N = len(str(X))
for i in range(K):
    X = Decimal(str(X/10)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

print(X*(10**K))