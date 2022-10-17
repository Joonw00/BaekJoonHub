import sys
n = input()
n = int(n)
g = []
dp = [[0 for i in range(3)] for j in range(n)]
for i in range(n):
    a = sys.stdin.readline().rstrip()
    a = int(a)
    g.append(a)
dp[0][1] = g[0]
for i in range(1,n):
    i = int(i)
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + g[i]
    dp[i][2] = dp[i-1][1] + g[i]
print(max(dp[n-1]))