

N = int(input())
N = hex(N)[2:]
if len(N) < 2:
    N = '0' + N

print(N.upper())