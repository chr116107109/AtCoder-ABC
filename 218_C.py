

N = int(input())
S = [input() for i in range(N)]
T = [input() for i in range(N)]

def be_slim(S):
    n = len(S[0])
    while not '#' in S[0]:
        S = S[1:]
    while not '#' in S[-1]:
        S = S[:-1]
    return S

def rot(S):
    tate = len(S)
    yoko = len(S[0])
    new_S = ['' for i in range(yoko)]
    for i in range(yoko):
        for j in range(tate-1,-1,-1):
            new_S[i] += S[j][i]

    return new_S

def main(S,T):
    S = be_slim(S)
    S = rot(S)
    S = be_slim(S)
    T = be_slim(T)
    T = rot(T)
    T = be_slim(T)
    for i in range(4):
        if S == T:
            print('Yes')
            return 
        T = rot(T)

    print('No')

main(S,T)