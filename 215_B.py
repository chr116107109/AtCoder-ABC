


N = int(input())

strN = str(N)
ketaN = [0] * len(strN)

K = N
for i in range(len(strN)):
    ketaN[i] = K//(10**(len(strN)-i-1))
    K = K - ketaN[i] * 10**(len(strN)-i-1)

b = 0
for i in range(80):
    str2 = str(2**i)


    #print(2**i)
    keta = len(str(str2))
    keta2 = [0] * keta

    K = 2**i
    for j in range(keta):
        keta2[j] = K//(10**(keta-j-1))
        K = K - keta2[j] * 10**(keta-j-1)

    #print(str2)
    #print(keta2)
    #print(ketaN)
    if len(keta2) > len(ketaN):
        print(i-1)
        break
    elif len(keta2) == len(ketaN):
        for j in range(keta):
            if keta2[j] == ketaN[j]:
                continue
            if keta2[j] < ketaN[j]:
                break
            if keta2[j] > ketaN[j]:
                print(i-1)
                #print('-- BREAK inner loop')
                b = 1
                break

        if b == 1:
            break
