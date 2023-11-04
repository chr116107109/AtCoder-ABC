import math


def isPrime(n):
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  
  # nの平方根まで計算する
  m = math.floor(math.sqrt(n)) + 1
  for p in range(3, m, 2):
      if n % p == 0:
        return False
  return True


[A,B,C,D] = list(map(int,input().split()))

frag1 = 0
for i in range(A,B+1):
    frag2 = 0
    for j in range(C,D+1):
        if isPrime(i+j):
            frag2 = 1

    if frag2 == 0:
        frag1 = 1

if frag1 == 1:
    print('Takahashi')
else:
    print('Aoki')