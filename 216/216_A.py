
S = input()

if S[-1] <= '2':
    print(S[:-2]+'-')
elif S[-1] <= '6':
    print(S[:-2])
else:
    print(S[:-2]+'+')

