import sys
from collections import deque

n = int(input())

pair = int(input())

adj = [[] for _ in range(n+1)]
for i in range(pair):
    a,b = map(int,sys.stdin.readline().split())

    adj[a].append(b)
    adj[b].append(a)

visited = [0 for _ in range(n+1)]


q = deque()
for i in range(len(adj[1])):
    q.append(adj[1][i])
visited[1] = 1
while q:
    node = q.popleft()
    visited[node] = 1
    l = len(adj[node])
    for i in range(l):
        nextNode = adj[node][i]
        if visited[nextNode] == 1:
            continue
        q.append(nextNode)
ans = 0
for i in range(n+1):
    if visited[i] == 1:
        ans+=1
print(ans-1)