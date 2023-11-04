import sys

S = input()
T = input()

if S == T:
    print('Yes')
else:
    for i in range(len(S)-1):
        S_ex = S[:i] + S[i+1] + S[i] + S[i+2:]
        #print(S_ex)
        if S_ex == T:
            print('Yes')
            sys.exit()

    print('No')
