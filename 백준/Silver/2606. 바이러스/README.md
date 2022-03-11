# [Silver III] 바이러스 - 2606 

[문제 링크](https://www.acmicpc.net/problem/2606) 

### 성능 요약

메모리: 30864 KB, 시간: 72 ms

### 분류

너비 우선 탐색(bfs), 깊이 우선 탐색(dfs), 그래프 이론(graphs), 그래프 탐색(graph_traversal)

##다른 풀이
graph = [[]*n for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
visited = [0]*(n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt +=1
dfs(1)

#이차원 배열엥 a,b기준으로 append해서 모체가 앞에오는 배열을 만듬
#이후 방문처리하는 방식으로 진행(dp?)
