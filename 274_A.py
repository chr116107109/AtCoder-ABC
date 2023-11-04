
A,B = map(int,input().split())

from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
from unicodedata import decimal

S = Decimal(str(B/A)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)
S = str(S) + '0'*(5-len(str(S)))

print(S)