from collections import deque
import sys
n,m,v = map(int,sys.stdin.readline().split())
graph = [[0 for _ in range(n+1)] for _ in range(n+1)]

#그래프 모양 생성
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1
#dfs 시작
dvisited = [0 for _ in range(n+1)]
def dfs(v):
    print(v,end=' ')
    dvisited[v] = 1
    for i in range(1,n+1):
        if graph[v][i] == 1 and dvisited[i] == 0:
            dfs(i)
bvisited = [0 for _ in range(n+1)]
def bfs(v):
    q = deque()
    q.append(v)
    bvisited[v] = 1
    while q:
        v = q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if graph[v][i] == 1 and bvisited[i] == 0:
                q.append(i)
                bvisited[i] = 1
dfs(v)
print()
bfs(v)