

X = input()

for i in range(5):
    if X[i] == '.':
        if int(X[i+1]) >= 5:
            ans = int(X[:i]) + 1
        elif int(X[i+1]) <= 4:
            ans = int(X[:i])


print(ans)
