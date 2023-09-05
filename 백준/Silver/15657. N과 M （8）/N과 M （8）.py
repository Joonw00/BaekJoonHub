import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
ans = []
arr.sort()
def dfs(depth, start, n, m):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, n):
        ans.append(arr[i])
        dfs(depth + 1, i, n, m)
        ans.pop()

dfs(0, 0, n, m)