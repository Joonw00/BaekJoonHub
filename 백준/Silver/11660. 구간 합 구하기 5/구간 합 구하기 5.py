import sys
n,m = map(int,sys.stdin.readline().split())
num = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    num.append(a)
dp = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            dp[i][j] = num[i][j]
        elif i == 0:
            dp[i][j] = num[i][j] + dp[i][j-1]
        elif j == 0:
            dp[i][j] = num[i][j] + dp[i-1][j]
        else:
            dp[i][j] = num[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        
for i in range(m):
    x1,y1,x2,y2 = list(map(int,sys.stdin.readline().split()))
    if x1 == 1 and y1 == 1:
        print(dp[x2-1][y2-1])
    elif x1 == 1:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2])
    elif y1 == 1:
        print(dp[x2-1][y2-1] - dp[x1-2][y2-1])
    else:
        print(dp[x2-1][y2-1] - dp[x2-1][y1-2] - dp[x1-2][y2-1] + dp[x1-2][y1-2])