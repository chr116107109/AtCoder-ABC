
S = input()

sent = ['dream','dreamer','erase','eraser']


length = len(S)
old= length
flag = True
while length > 0:
    for s in sent:
        if s == S[length-len(s):length]:
            length -= len(s)
    if old == length:
        flag = False
        break
    old = length

if flag:
    print('YES')
else:
    print('NO')