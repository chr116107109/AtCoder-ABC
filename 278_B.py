import sys
H,M = map(int,input().split())


for h in range(24):
    for m in range(60):
        sh = str(H)
        sm = str(M)
        if len(sh) < 2:
            sh = '0'+ sh
        if len(sm) < 2:
            sm = '0'+ sm

        if 0 <= int(sh[0]+sm[0]) <= 23 and 0 <= int(sh[1]+sm[1]) <= 59:
            print(H,M)
            sys.exit()
        
        M += 1
        if M == 60:
            H += 1
            H %= 24
        M %= 60
        