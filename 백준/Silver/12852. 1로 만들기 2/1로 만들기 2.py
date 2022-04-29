import sys
N = input()
N = int(N)

dp = [[10**7,-1] for _ in range(3*N + 3)]
dp[1][0] = 0
for i in range(1,N):
  i = int(i)

  if dp[i+1][0] > dp[i][0]+1:
    dp[i+1][0] = dp[i][0]+1
    dp[i+1][1] = 1

  if dp[i*2][0] > dp[i][0]+1:
    dp[i*2][0] = dp[i][0]+1
    dp[i*2][1] = 2

  if dp[i*3][0] > dp[i][0]+1:
    dp[i*3][0] = dp[i][0]+1
    dp[i*3][1] = 3

print(dp[N][0])
while N != 1:
  print(N,end=" ")
  if dp[N][1] == 1:
    N-=1
  elif dp[N][1] == 2:
    N=N//2
  elif dp[N][1] == 3:
    N=N//3
print(1)