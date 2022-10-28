import sys
sys.setrecursionlimit(10**5)
n = input()
n = int(n)
def dfs(start):
    for i in gph[start]:
        if visited[i] == 0:
            visited[i] = start
            dfs(i)
gph = [[] for _ in range(n+1)]
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    gph[a].append(b)
    gph[b].append(a)
visited = [0]*(n+1)

dfs(1)
for i in range(2,n+1):
    print(visited[i])