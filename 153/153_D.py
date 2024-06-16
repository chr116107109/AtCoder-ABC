
H = int(input())

def solve(X):
    if X == 1:
        return 1
    
    return 1+2*solve(X//2)

print(solve(H))
