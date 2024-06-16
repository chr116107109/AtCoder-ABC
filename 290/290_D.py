

def solve():
    N,D,K = map(int,input().split())
    D %= N
    if N%D == 0:
        K -= 1
        mod = K//D
        K %= D

        print(K*D + mod)
    else:
        mod = 0
        while K > 0:
            if mod <= N%D:
                if K < N//D+1:
                    break
                K -= N//D+1
            else:
                K -= N//D


T = int(input())

for i in range(T):
    solve()