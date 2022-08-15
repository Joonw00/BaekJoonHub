import sys
n=int(input())
mp = []
for i in range(n):
    mp.append(sys.stdin.readline())
visited = [[False for _ in range(n)] for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(i,j):
    if visited[i][j]:
        return
    if mp[i][j] == '0':
        return
    visited[i][j] = True
    ans[-1]+=1
    for k in range(4):
        if 0<=i+dx[k]<n and 0<=j+dy[k]<n:
            dfs(i+dx[k],j+dy[k])
ans = []
for i in range(n):
    for j in range(n):
        if mp[i][j] == '1' and visited[i][j] == False:
            ans.append(0)
            dfs(i, j)
            
ans.sort()
print(len(ans))
for i in ans:
    print(i)
