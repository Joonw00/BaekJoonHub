import sys
N,M = map(int,sys.stdin.readline().split())
fr = [[] for _ in range(N)]
for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    fr[a].append(b)
    fr[b].append(a)
ans = False
visited = [False]*N
def dfs(v,h):
    global ans
    visited[v] = True
    if h == 4:
        ans = True
        return
    for i in fr[v]:
        if not visited[i]:
            dfs(i,h+1)
            visited[i] = False

for i in range(N):
    dfs(i,0)
    visited[i] = False
if ans:
    print(1)
else:
    print(0)