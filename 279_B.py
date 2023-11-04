
S = input()
T = input()

if len(S) < len(T):
    print('No')
else:
    ans ='No'
    for i in range(len(S)-len(T)+1):
        if S[i:i+len(T)] == T:
            ans = 'Yes'
            break
    print(ans)