import sys
n,m =map(int, sys.stdin.readline().split())

sqr = []
for i in range(n):
  sqr.append(sys.stdin.readline().rstrip())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
ans = []
ans.append(0)
for i in range(1,n+1):
  i = int(i)
  for j in range(1,m+1):
    j = int(j)
    if sqr[i-1][j-1] == '0':
      dp[i][j] = 0
    elif sqr[i-1][j-1] == '1':
      dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    
    ans.append(dp[i][j])

m = max(ans)
print(m**2)