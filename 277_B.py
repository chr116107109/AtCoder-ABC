
N = int(input())
T = [input() for i in range(N)]

def main():
    d = set()
    for S in T:
        #print(S,d)
        if S[0] in {'H','D','C','S'} and S[1] in {'A','2','3','4','5','6','7','8','9','T','J','Q','K'} and (not (S in d)):
            d.add(S)
            continue
        else:
            print('No')
            return

    print('Yes')

main()