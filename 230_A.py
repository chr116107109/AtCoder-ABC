
N = int(input())

if N < 42:
    ans = N
else:
    ans = N + 1

s = str(ans)

if len(s) == 1:
    ans = 'AGC00' +  s
elif len(s) == 2:
    ans = 'AGC0' + str(ans)

print(ans)
