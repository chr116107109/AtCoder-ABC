
d = {'a':0,'t':1,'c':2,'o':3,'d':4,'e':5,'r':6}

S = list(input())
count = 0
for i in range(7):
    for j in range(6):
        if d[S[j]] > d[S[j+1]]:
            S[j],S[j+1] = S[j+1],S[j]
            count += 1
            #print(S)

print(count)