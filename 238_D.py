
T = int(input())

def solve(a,s):
    y = s - a
    if y < 0:
        return False 
    return y&a == a

for i in range(T):
    a,s = map(int,input().split())
    if solve(a,s):
        print('Yes')
    else:
        print('No')
