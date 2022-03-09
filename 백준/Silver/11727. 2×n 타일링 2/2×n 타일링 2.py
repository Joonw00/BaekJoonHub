import sys
N = input()
N = int(N)

#1,2를 이용해 N을 만들 수 있는 가짓 수
dp = [0]*N
dp[0]=1
if N>1:
    dp[1]=2
for i in range(N):
    if i+1 < N:
        dp[i+1]+=dp[i]
    if i+2 < N:
        dp[i+2]+=dp[i] * 2
print(dp[N-1]%10007)