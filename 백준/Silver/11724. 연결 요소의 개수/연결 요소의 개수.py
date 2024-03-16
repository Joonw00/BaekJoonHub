from collections import deque
import sys
N,M = map(int, sys.stdin.readline().split())
graph = []

#입력 받은 값들 저장할 공간
for i in range(N+1):
    graph.append([])
#정보 받기
for i in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    #양방향 처리
count = 0   #정답
visited = [False]*(N+1)



def bfs(graph,start,visited):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

for i in range(1,N+1):
    i = int(i)
    if len(graph[i])!=0 and visited[i] == False:
        bfs(graph,i,visited)
        count+=1
    #혼자만 있는 경우 처리해야되나??
    elif len(graph[i]) == 0:
        count+=1

print(count)