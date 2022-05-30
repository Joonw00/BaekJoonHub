import sys
N,K = map(int,sys.stdin.readline().split())
#n까지 k개합의 경우의 수
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(N+1):
    dp[i][1] = 1
#범위 재설정 필요
for i in range(N+1):
    #i이후의 수j들은
    for j in range(i,N+1):
        for k in range(1,K):
            k = int(k)
            dp[j][k+1] += dp[i][k]
print(dp[N][K]%1000000000)