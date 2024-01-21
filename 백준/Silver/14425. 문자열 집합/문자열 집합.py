import sys

n,m = map(int, sys.stdin.readline().split())
s = set()
for i in range(n):
    s.add(sys.stdin.readline().strip())
ans = 0
l = len(s)
for i in range(m):
    t = sys.stdin.readline().strip()
    s.add(t)
    if len(s) == l:
        ans += 1
    else:
        s.remove(t)
print(ans)
