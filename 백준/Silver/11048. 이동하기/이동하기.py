import sys
n,m = map(int,sys.stdin.readline().split())
maze = []
dp = [[0]*m for _ in range(n)]
for i in range(n):
    maze.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if i ==0 and j ==0:
            dp[i][j] = maze[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + maze[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + maze[i][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + maze[i][j]
print(dp[n-1][m-1])