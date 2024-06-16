

N = int(input())

S = [input() for i in range(N)]
ans = 10**10

for i in range(10):
    time = 0
    count = N
    stop = [0] * N
    while count > 0:
        
        for k in range(N):

            if S[k][time%10] == str(i) and stop[k] == 0:
                #print(i,k,time)
                stop[k] = 1
                count -= 1
                break
        
        time += 1

    #print(time)
    
    ans = min(ans,time-1)

print(ans)