import sys
import copy 
from collections import deque
N,M = map(int,sys.stdin.readline().split())

def bfs(w1,w2,w3):
  clab = copy.deepcopy(lab)
  clab[w1[0]][w1[1]] = 1
  clab[w2[0]][w2[1]] = 1
  clab[w3[0]][w3[1]] = 1
  vir = deque()
  for e in v:
    vir.append(e)
  dx = [-1,1,0,0]
  dy = [0,0,1,-1]
  while vir:
    b,a = vir.popleft()
    for d in range(4):
      y = b+dy[d]
      x = a+dx[d]
      if 0<=x<M and 0<=y<N and clab[y][x] == 0:
        clab[y][x] = 2
        vir.append([y,x])
  count = 0
  for a in range(N):
    for b in range(M):
      if clab[a][b] == 0:
        count+=1
  return count

lab = []
for i in range(N):
  lab.append(list(map(int,sys.stdin.readline().split())))

v = []
for i in range(N):
  for j in range(M):
    if lab[i][j] == 2:
      v.append([i,j])

ans = 0
for i in range(N*M-2):
  w1 = [i//M,i%M]
  if lab[w1[0]][w1[1]] != 0:
    continue

  for j in range(i+1,N*M-1):
    j = int(j)
    w2 = [j//M,j%M]
    if lab[w2[0]][w2[1]] != 0:
      continue

    for k in range(j+1,N*M):
      k = int(k)
      w3 = [k//M,k%M]
      if lab[w3[0]][w3[1]] != 0:
        continue

      ans = max(bfs(w1,w2,w3),ans)  
print(ans)