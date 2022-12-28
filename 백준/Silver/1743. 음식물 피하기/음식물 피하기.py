import sys
sys.setrecursionlimit(100000)
global cnt
n,m,k = map(int,sys.stdin.readline().split())
loc = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
    r,c = map(int,sys.stdin.readline().split())
    loc[r-1][c-1] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[0 for _ in range(m)] for _ in range(n)]
def dfs(x,y):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if loc[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx,ny)
                cnt+=1
ans = 0
for i in range(n):
    for j in range(m):
        if loc[i][j] == 1 and visited[i][j] == 0:
            cnt = 1
            dfs(i,j)
            ans = max(ans,cnt)
print(ans)