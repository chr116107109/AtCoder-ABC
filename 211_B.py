

S1 = str(input())
S2 = str(input())
S3 = str(input())
S4 = str(input())

S = [S1,S2,S3,S4]

#print(S)

key = ['H' , '2B' , '3B' , 'HR']

dict = dict(zip(key,[0,0,0,0]))

for i in S:
    dict[i] = 1

NO = 0
for i in key:
    if dict[i] == 0:
        print('No')
        NO = 1
        break


if NO == 0:
    print('Yes')
