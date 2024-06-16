
K = int(input())

if K >= 60:
    if K >= 70:
        S = '22:' + str(K-60)
    else:
        S = '22:0' + str(K-60)
else:
    if K >= 10:
        S = '21:' + str(K)
    else:
        S = '21:0' + str(K)


print(S)