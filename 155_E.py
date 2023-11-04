

N = input()

ans = 0 

agari = 0 
for i in N:
    n = int(i)
    if n <= 5:
        ans += n
    else:
        if agari == 0:
            ans += 11-n
            agari += 1
        else:
            ans += 10-n
            ans -= 1
            agari -= 1

print(ans)