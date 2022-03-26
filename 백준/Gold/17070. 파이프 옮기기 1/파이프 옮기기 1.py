import sys
N = input()
N = int(N)
house = []
for i in range(N):
    a = list(map(int,sys.stdin.readline().split()))
    house.append(a)
#가로0,대각1,세로2
dp = [[[0 for _ in range(3)] for _ in range(N)]for _ in range(N)]

dp[0][1][0] = 1
for i in range(N):
    for j in range(1,N):
        j = int(j)
        if house[i][j] == 1:
            continue
        if i == 0 and j==1:
            continue
        #가로
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
        #세로
        if i == 0:
            continue
        dp[i][j][2] = dp[i-1][j][2] + dp[i-1][j][1]

        #대각
        if house[i-1][j] == 1 or house[i][j-1] == 1:
            continue
        dp[i][j][1] = dp[i-1][j-1][0] +dp[i-1][j-1][1] + dp[i-1][j-1][2]

ans = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]    

print(ans)