


from re import I, L


s = [[0]*3 for i in range(3)]
h1,h2,h3,w1,w2,w3 = map(int,input().split())
count = 0
for i in range(1,29):
    for j in range(1,29):
        for k in range(1,29):
            for l in range(1,29):
                s[0][0] = i
                s[0][1] = j
                s[0][2] = h1 - i - j
                s[1][0] = k
                s[1][1] = l
                s[1][2] = h2 - k - l
                s[2][0] = w1 - i - k 
                s[2][1] = w2 - j - l
                #s[2][2] = w3 - s[2][0] - s[2][1]
                #print(s)
                #print(s[0][2] + s[1][2] + (w3 - s[2][0] - s[2][1]))
                #print(s[2][0] + s[2][1] + (h3 - s[0][2] - s[1][2]))
                frag = 1
                for x in range(3):
                    for y in range(3):
                        if x != 2 or y!= 2:
                            if s[x][y] <= 0:
                                frag = 0
                if frag == 0:
                    continue

                if (h3 - s[2][0] - s[2][1] > 0) and (s[0][2] + s[1][2] + (h3 - s[2][0] - s[2][1]) == w3):
                    count += 1
                    #print(s)
#                elif (w3 - s[0][2] - s[1][2] > 0) and s[2][0] + s[2][1] + (w3 - s[0][2] - s[1][2]) == h3:
#                    count += 1

print(count)

