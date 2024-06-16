
S = input()

if S.islower() or S.isupper() or len(set(S)) < len(S):
    print('No')
else:
    print('Yes')