import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())

wall = []
for i in range(n):
  wall.append(sys.stdin.readline().rstrip())


#[경로,벽뿌]
visited = [[[0,0] for _ in range(m)]for _ in range(n)]
visited[0][0][0] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
q.append([0,0,0])
ans = 0
while q:
  a,b,w = q.popleft()
  if b == n-1 and a == m-1:
    ans = 1
    break

  for k in range(4):
    x  = a+dx[k]
    y = b+dy[k]

    if 0<=x<m and 0<=y<n:
      if wall[y][x] == '0' and visited[y][x][w] == 0:
        visited[y][x][w] = visited[b][a][w] + 1
        q.append([x,y,w])
      elif wall[y][x] == '1' and w == 0:
        visited[y][x][1] = visited[b][a][0] + 1
        q.append([x,y,1])

if n == 1 and m == 1:
  print(1)
else:
  if ans == 0:
    print(-1)
  else:
    print(visited[n-1][m-1][w])