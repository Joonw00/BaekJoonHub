import sys
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
s3 = sys.stdin.readline().rstrip()
dp = [[[0 for _ in range(1+len(s1))]for _ in range(1+len(s2))] for _ in range(1+len(s3))]
for i in range(1,1+len(s3)):
  i = int(i)
  for j in range(1,1+len(s2)):
    j = int(j)
    for k in range(1,1+len(s1)):
      k = int(k)
      if s1[k-1] == s2[j-1] and s2[j-1] == s3[i-1]:
        dp[i][j][k] = dp[i-1][j-1][k-1]+1 
      else:
        dp[i][j][k] = max(dp[i-1][j][k] ,dp[i][j-1][k], dp[i][j][k-1])
m = 0
for k in range(1+len(s3)):
  for i in range(1+len(s2)):
    for j in range(1+len(s1)):
      m = max(m, dp[k][i][j])
print(m)

