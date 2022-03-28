import sys
N = input()
N = int(N)
INF = 1000000
ans = INF
cost = []
for i in range(N):
    r,g,b = map(int, sys.stdin.readline().split())
    cost.append([r,g,b])

for j in range(3):
    c = [[INF, INF, INF] for _ in range(N)]
    c[0][j] = cost[0][j]
    
    for i in range(1,N):
        i = int(i)
        c[i][0] = cost[i][0] + min(c[i-1][1],c[i-1][2])
        c[i][1] = cost[i][1] + min(c[i-1][0],c[i-1][2])
        c[i][2] = cost[i][2] + min(c[i-1][0],c[i-1][1])
    for i in range(3):
        if i != j:
            ans = min(ans, c[N-1][i])


print(ans)
    