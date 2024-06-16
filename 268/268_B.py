
S = input()
T = input()

if len(T) < len(S):
    print("No")
else:
    if S == T[:len(S)]:
        print('Yes')
    else:
        print('No')