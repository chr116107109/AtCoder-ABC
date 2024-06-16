
K = int(input())

strbinK = str(bin(K)[2:])

ans = ''
for i in range(len(strbinK)):
    if strbinK[i] == '1':
        ans += '2'
    else:
        ans += '0'


print(ans)
