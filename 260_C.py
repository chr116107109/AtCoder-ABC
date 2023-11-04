
N,X,Y = map(int,input().split())

def dfs(N,color):
    if N == 1:
        if color == 'r':
            return 0
        if color == 'b':
            return 1
    
    if color == 'r':
        return dfs(N-1,'r') + X*dfs(N,'b')
    if color == 'b':
        return dfs(N-1,'r') + Y*dfs(N-1,'b')

print(dfs(N,'r'))