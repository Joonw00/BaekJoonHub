from re import X
import sys
l = input()
l = int(l)
A = list(map(int, sys.stdin.readline().split()))
dp = [1]*l

for i in range(l):
    for j in range(i):
        if A[i]>A[j] and dp[i] < dp[j]+1:   #비교 대상이 더 크다면
            dp[i] = dp[j]+1
print(max(dp))