
N = int(input())

m = 1
num = 1
while N > m:
    if m > 1:
        N -= m
        num += 1 
    m *= 26
ans = []
print(N,num)

while num > 0:
    print(N)
    ans.append(chr(96+N//pow(26,num-1)))

    N %= pow(26,num-1)
    N -= 1
    num -= 1

print("".join(ans))