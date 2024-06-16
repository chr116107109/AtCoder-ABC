
S = input()

if 65<=ord(S[0])<=90 and 65<=ord(S[-1])<=90 and '100000'<=S[1:-1]<='999999':
    print('Yes')
else:
    print('No')