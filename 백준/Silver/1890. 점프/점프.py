import sys
n = int(sys.stdin.readline())
m = []
for i in range(n):
    m.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = 1
        if m[i][j] == 0:
            continue
        if i + m[i][j] < n:
            dp[i + m[i][j]][j] = dp[i + m[i][j]][j] + dp[i][j]
        if j + m[i][j] < n:
            dp[i][j + m[i][j]] = dp[i][j + m[i][j]] + dp[i][j]
print(dp[n - 1][n - 1])