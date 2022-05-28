import sys
T = input()
T = int(T)
for _ in range(T):
  N,L,R = map(int,sys.stdin.readline().split())
  #좌,우,총
  dp = [[[0 for _ in range(N+1)] for _ in range(N+1)] for _ in range(N+1)]
  dp[1][1][1] = 1
  for i in range(2,N+1):
    i = int(i)
    for l in range(1,i):
      l = int(l)
      for r in range(1,i-l+1):
        r = int(r)
        dp[l+1][r][i] +=dp[l][r][i-1]
        dp[l][r+1][i] +=dp[l][r][i-1]
        dp[l][r][i] +=(i-2) * dp[l][r][i-1]
  ans = dp[L][R][N]
  print(ans)