import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = sys.maxsize
graph = [[inf for _ in range(n)] for _ in range(n)]
for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = min(graph[a-1][b-1], c)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
for i in range(n):
    for j in range(n):
        if graph[i][j]==inf:
            graph[i][j] = 0

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=' ')
    print()

