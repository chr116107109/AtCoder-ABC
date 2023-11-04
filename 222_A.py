
N = input()

if len(N) == 4:
    print(N)

else:
    for i in range(3):
        N = '0' + N
        if len(N) == 4:
            print(N)
            break
