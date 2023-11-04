
S1 = input()
S2 = input()
S3 = input()

import itertools
if len(set(S1+S2+S3)) > 10:
    print('UNSOLVABLE')
else:
    S = set(S1+S2+S3)
    T = ['0'] * 26
    for p in itertools.permutations(('0','1','2','3','4','5','6','7','8','9')):

        for i,n in enumerate(S):
            T[ord(n)-97] = p[i]
        if T[ord(S1[0])-97] == '0' or T[ord(S2[0])-97] == '0' or T[ord(S3[0])-97] == '0':
            continue
        N1 = int(''.join([T[ord(n)-97] for n in S1]))
        N2 = int(''.join([T[ord(n)-97] for n in S2]))
        N3 = int(''.join([T[ord(n)-97] for n in S3]))

        if N3 == N1+N2:
            print(N1)
            print(N2)
            print(N3)
            break
    else:
        print('UNSOLVABLE')