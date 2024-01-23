import sys
from collections import deque

n = int(sys.stdin.readline().strip())
rg = []
rgb = []
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    rg.append(temp.replace('R','G'))
    rgb.append(temp)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(y,x):
    q = deque()
    if check[y][x] == 1:
        return
    q.append([y,x])
    check[y][x] = 1

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and rgb[ny][nx] == rgb[y][x]:
                q.append([ny,nx])
                check[ny][nx] = 1

def bfsrg(y,x):
    q = deque()
    if check[y][x] == 1:
        return
    q.append([y,x])
    check[y][x] = 1

    while q:
        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n and check[ny][nx] == 0 and rg[ny][nx] == rg[y][x]:
                q.append([ny,nx])
                check[ny][nx] = 1


check = [[0]*n for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            bfs(i,j)
            ans += 1


check = [[0]*n for _ in range(n)]
ansrg = 0
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            bfsrg(i,j)
            ansrg += 1

print(ans,ansrg)