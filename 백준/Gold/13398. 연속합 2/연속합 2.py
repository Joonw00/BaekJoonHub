import sys
n = input()
n = int(n)
A = list(map(int, sys.stdin.readline().split()))
dp = [[-10000 for i in range(n+1)] for _ in range(2)]
dp[0][0] = A[0]
dp[1][0] = A[0]
for i in range(1,n):
    i = int(i)
    dp[0][i] = max(A[i], dp[0][i-1] + A[i])
    dp[1][i] = max(dp[1][i-1] + A[i], dp[0][i-1])
print(max(max(dp[0]),max(dp[1])))