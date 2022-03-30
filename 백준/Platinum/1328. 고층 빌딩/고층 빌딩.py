import sys
N,L,R = input().split()
N = int(N)
L = int(L)
R = int(R)

#100대신 101로 설정한 거 기억해야 됨
dp = [[[0 for _ in range(101)]for _ in range(101)]for _ in range(101)]
dp[1][1][1] = 1

#배치될 건물의 수 i (배치 후)
for i in range(2,N+1):
    i = int(i)
    #l,r은 배치 전
    for l in range(1,i):
        l = int(l)
        for r in range(1,i- l +1):
            r = int(r)
            dp[i][l+1][r] += dp[i-1][l][r]
            dp[i][l][r+1] += dp[i-1][l][r]
            dp[i][l][r] += (i-2) * dp[i-1][l][r]


#제출
ans = dp[N][L][R]
print(ans%1000000007)