import sys
l = input()
l = int(l)
A = list(map(int, sys.stdin.readline().split()))
sum = []

dp = [1]*l

for i in range(l):
    for j in range(i):
        if A[i]<A[j] and dp[i] < dp[j]+1:  #and이전: 감소하고,+예외처리
            dp[i]=dp[j]+1

print(max(dp))