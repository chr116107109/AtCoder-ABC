
N = int(input())

AB = [list(map(int,input().split())) for i in range(N)]

C = [A[0]/A[1] for A in AB]

sum = 0
sumC = 0
for i in range(N):
    sum += AB[i][0]
    sumC += C[i]


ans = sum/2

for i in range(100):
    left = ans
    right = sum - ans

    timel = 0
    for j in range(N):
        if left >= AB[j][0]:
            left -= AB[j][0]
            timel += C[j]
            #print('timel {}'.format(timel))
        elif left < AB[j][0]:
            timel += left/AB[j][1]
            #print('timel {}'.format(timel))
            break
    timer = 0
    for j in range(N-1,-1,-1):
        if right >= AB[j][0]:
            right -= AB[j][0]
            timer += C[j]
            #print('timer {}'.format(timer))
        elif right < AB[j][0]:
            timer += right/AB[j][1]
            #print('timer {}'.format(timer))
            break

    if timel > timer:
        ans = ans - sum/(2**(2+i))
    else:
        ans = ans + sum/(2**(2+i))

print(ans)
