import sys
N = input()
N = int(N)
P = list(map(int, sys.stdin.readline().split()))
cost = [0]*(2*N+1)
for i in range(N+1):
    for j in range(1, N+1):
        if i+j > N:
            break
        if cost[i+j] < cost[i] + P[j-1]:
            cost[i+j] = cost[i] + P[j-1]
print(cost[N])