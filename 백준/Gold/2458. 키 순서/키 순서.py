import sys
n,m = map(int, sys.stdin.readline().split())
inf = sys.maxsize
graph = [[inf for _ in range(n)] for _ in range(n)]
for i in range(m):
    # a<b
    a,b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                graph[i][j] = 0
            else:
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
cnt = 0
for i in range(n):
    flag = True
    for j in range(n):
        if graph[i][j]==inf and graph[j][i]==inf:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt)