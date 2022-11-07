import sys
n,m = map(int,sys.stdin.readline().split())
cheeze = []
for i in range(n):
    cheeze.append(list(map(int,sys.stdin.readline().split())))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
#공기를 2로
def bfs(x,y):
    q = []
    q.append([x,y])
    while q:
        x,y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                if cheeze[nx][ny] == 0 or cheeze[nx][ny] == 2:
                    cheeze[nx][ny] = 2
                    q.append([nx,ny])
                    visited[nx][ny] = 1
#치즈를 0으로 녹임
def melt():
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if cheeze[nx][ny] == 2:
                        cheeze[i][j] = 0
                        break
def check():
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                return True
    return False
def count():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] == 1:
                cnt += 1
    return cnt


time = 0
while True:
    if check() == False:
        break
    visited = [[0]*m for _ in range(n)]
    bfs(0,0)
    ans = count()
    melt()
    time += 1
    
print(time)

print(ans)