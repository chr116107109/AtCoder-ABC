

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

from collections import Counter
Ac = Counter(A)
Bc = Counter(B)

if Ac != Bc:
    print("No")
else:
    ans = "No"
    for a in Ac:
        if Ac[a] >=2:
            ans = "Yes"
    for a in Bc:
        if Bc[a] >=2:
            ans = "Yes"
    
    print(ans)
