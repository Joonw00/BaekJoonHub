import sys
n = int(sys.stdin.readline())
tr = []
for i in range(n):
    tr.append(list(map(int, sys.stdin.readline().split())))
dp = [[0] * (n+1) for _ in range(n+1)]
dp[0][0] = tr[0][0]
for i in range(n-1):
    i = int(i)
    for j in range(i+1):
        dp[i+1][j] = max(dp[i+1][j], tr[i+1][j]+dp[i][j])
        dp[i+1][j+1] = max(dp[i+1][j+1], tr[i+1][j+1]+dp[i][j])
        
print(max(dp[-2]))
