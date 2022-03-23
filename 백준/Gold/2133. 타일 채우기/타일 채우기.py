N = input()
N = int(N)
dp = [0]*31
dp[0] = 1
for i in range(31):
    if i !=0 and dp[i] == 0:
        continue
    if i+2<31:
        dp[i+2] += 3*dp[i]
    k = i+4
    while k<31:
        dp[k] += 2*dp[i]
        k+=2
print(dp[N])