import sys
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
dp = [[0 for _ in range(1+len(s1))]for _ in range(1+len(s2))]
for i in range(1,1+len(s2)):
  i = int(i)
  for j in range(1,1+len(s1)):
    j = int(j)
    if s1[j-1] == s2[i-1]:
      dp[i][j] = dp[i-1][j-1]+1
    else:
      dp[i][j] = max(dp[i-1][j],dp[i][j-1])
m = 0
for i in range(1+len(s2)):
  for j in range(1+len(s1)):
    m = max(m, dp[i][j])
print(m)
