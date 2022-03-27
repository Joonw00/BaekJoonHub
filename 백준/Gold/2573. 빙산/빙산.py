import sys
from collections import deque
N,M = input().split()
N = int(N)
M = int(M)

def chk(y,x):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    q = deque()
    q.append([y,x])
    while q:
        y,x = q.popleft()
        visited[y][x] = True
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= ny < N and 0 <= nx < M:
                if ice[ny][nx] != 0 and visited[ny][nx] == False:
                    q.append([ny,nx])
                    visited[ny][nx] = True
                elif ice[ny][nx] == 0:
                    count[y][x] += 1
    return 1
a = 0

ice = []
for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    ice.append(a)
t = 0
while True:
    visited = [[False]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    result = 0 
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0 and visited[i][j] == False:
                result += chk(i,j)
    #result : 한덩어리면 1, 여러 덩어리면 2

    for i in range(N):
        for j in range(M):
            ice[i][j]-=count[i][j]
            if ice[i][j] < 0:
                ice[i][j] = 0
    if result == 0:
        break
    if result >= 2:
        a = 1
        break


    t+=1

if a == 1:
    print(t)
else:
    print(0)