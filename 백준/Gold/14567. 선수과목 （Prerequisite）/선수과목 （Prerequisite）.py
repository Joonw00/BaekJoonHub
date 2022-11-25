import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
in_degree = [0] * (n+1)
dp = [0] * (n+1)
graph = [[] for _ in range(n+1)]
#입력 받고, 진입차수와 그래프 만들기
for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    in_degree[b] += 1
q = deque()
#진입차수가 0인 노드를 큐에 넣기
for i in range(1,n+1):
    if in_degree[i] == 0:
        q.append(i)
        dp[i] = 1
#큐가 빌 때까지 반복
while q:
    now = q.popleft()
    for i in graph[now]:
        in_degree[i] -= 1
        dp[i] = max(dp[i],dp[now]+1)
        if in_degree[i] == 0:
            q.append(i)
for i in range(1,n+1):
    print(dp[i],end=" ")

