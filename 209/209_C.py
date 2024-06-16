

N = int(input())
C = list(map(int, input().split()))


ans = 0
p = 1

pi = 1
if N==1:
    ans == C[0]

else:
    for i in range(1,C[0]+1):
        pi = 1
        for j in range(2,N+1):
            pi = pi * (C[j-1]-(i+j-1)+1)
            print('C_j is',C[j-1],'pi is',pi,i,j)

        ans = ans + pi
        print('ans is',ans)



print(ans)
