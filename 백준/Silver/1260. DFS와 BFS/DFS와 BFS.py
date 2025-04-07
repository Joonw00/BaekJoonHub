from collections import deque
import sys
def bfs(v):
    global visited, graph
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        temp = q.popleft()
        print(temp, end=" ")
        l = len(graph[temp])
        for i in range(l):
            if visited[graph[temp][i]] == True:
                continue
            q.append(graph[temp][i])
            visited[graph[temp][i]] = True

def dfs(v):
    global visited, graph
    if visited[v] == True:
        return
    visited[v] = True
    print(v, end=" ")
    for node in graph[v]:
        dfs(node)


n,m,v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    graph[i].sort()


visited = [False] * (n+1)
dfs(v)
print()
visited = [False] * (n+1)
bfs(v)