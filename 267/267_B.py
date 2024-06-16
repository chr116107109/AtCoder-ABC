
S = input()

pin = [0] * 7

import itertools

if S[0] == '1':
    print('No')
else:
    for i in range(2,11):
        if i == 2 or i == 8:
            if S[i-1] == '1':
                pin[2] += 1
        if i == 3 or i == 9:
            if S[i-1] == '1':
                pin[4] += 1
        if i == 7:
            if S[i-1] == '1':
                pin[0] += 1
        if i == 4:
            if S[i-1] == '1':
                pin[1] += 1
        if i == 5:
            if S[i-1] == '1':
                pin[3] += 1
        if i == 6:
            if S[i-1] == '1':
                pin[5] += 1
        if i == 10:
            if S[i-1] == '1':
                pin[6] += 1
    
    frag = False
    for i in range(7):
        for j in range(i+1,7):
            for k in range(i+1,j+1):
                if pin[i] > 0 and pin[j] >0 and pin[k] == 0:
                    frag = True
                    break
    if frag:
        print('Yes')
    else:
        print('No')
