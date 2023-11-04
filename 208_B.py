import math

P = int(input())

fac = [math.factorial(i) for i in range(1,11)]
ans = 10
#print(fac)
maisu = 0
for i in range(10):

    x = math.factorial(10-i)

    if P>=x:
        maisu = maisu + P//x
        #print(10-i,'! is',P//x,'mai','nokori',P - x*(P//x),'yen')
        P = P - x*(P//x)



print(maisu)
