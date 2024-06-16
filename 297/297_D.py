

A,B = map(int,input().split())

count = 0
while A != B:
    A,B = min(A,B),max(A,B)
    #print(A,B)
    if B%A == 0:
        count += B//A-1
        break
    count += B//A
    B %= A

print(count)