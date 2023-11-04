

from collections import deque

[a,N] = list(map(int,input().split()))

Q = deque()
Q.append(1)

inf = 2**20
dist = {1:0}

i=0
frag = 0
while i < inf and len(Q)>0:
  x = Q.popleft()
  #print(x,dist[x])

  if x == N:
      print(dist[x])
      frag = 1
      break

  x1 = a*x
  if len(str(x1)) <= len(str(N)):
      if not (x1 in dist.keys()):
          dist[x1] = dist[x] + 1
          Q.append(x1)

  if str(x)[-1] != '0':
      s = str(x)
      x2 = int(s[-1] + s[:-1])

      if not (x2 in dist.keys()):
          dist[x2] = dist[x] + 1
          Q.append(x2)
  i += 1

if frag == 0:
    print(-1)
