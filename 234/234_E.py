
X = input()

n = len(X)
a = int(X[0])

ans = 10**20
frag2 = 0
for i in range(-9,10):
    d = [a]
    frag = 0
    for j in range(n-1):
        if d[j] + i >= 0 and d[j] + i < 10 :
            d += [d[j]+i]
        else:
            frag = 1
            break

    if frag == 0:
        d_num = ''
        for i in range(n):
            d_num += str(d[i])
        d_num = int(d_num)
        #print(d_num)

        if d_num >= int(X) and d_num < ans:
            frag2 = 1
            ans = d_num

if frag2 == 0:
    if a == 9:
        a = 1
        X = '10' + X[1:]
        n += 1
    else:
        a += 1

    for i in range(-9,10):
        d = [a]
        frag = 0
        for j in range(n-1):
            if d[j] + i >= 0 and d[j] + i < 10 :
                d += [d[j]+i]
            else:
                frag = 1
                break

        if frag == 0:
            d_num = ''
            for i in range(n):
                d_num += str(d[i])
            d_num = int(d_num)
            #print(d_num)

            if d_num >= int(X) and d_num < ans:
                frag2 = 1
                ans = d_num




print(ans)
