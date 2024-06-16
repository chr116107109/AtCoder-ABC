
S = input()
T = input()

def main():
    for i in range(len(S)):
        if S[i] != T[i]:
            print(i+1)
            return

    print(len(T))

main()

