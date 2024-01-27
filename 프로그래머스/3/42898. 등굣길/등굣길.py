def solution(m, n, puddles):
    answer = 0
    dp = [[0 for i in range(m)]for j in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue
            if [j+1,i+1] in puddles:
                continue
            if i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    answer = dp[-1][-1] %1000000007
    return answer