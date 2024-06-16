
N = int(input())

a = list(map(int,input().split())) 

now_p = a[0]

now_l = 1
length = 0

d = [[a[0],1]]

print(1)
for i in range(1,N):
    if a[i] == now_p:
        now_l += 1
        d.append([now_p,now_l])
        for j in range(N):
            if now_p == now_l:
                del d[-now_p:]
                if d == []:
                    now_p = -1
                    now_l = 0
                    break
                else:
                    now_p = d[-1][0]
                    now_l = d[-1][1]
            else:
                break        
    else:
        now_p = a[i]
        now_l = 1
        d.append([now_p,now_l])

    #print(d)
    print(len(d))
    

