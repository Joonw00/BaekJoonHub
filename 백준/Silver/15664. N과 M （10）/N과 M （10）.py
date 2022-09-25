from itertools import combinations
import sys
n,m = map(int,sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))

visited = []
for a in combinations(seq,m):
    a = list(a)
    a.sort()
    if a not in visited:
        visited.append(a)
visited.sort()
for i in visited:
    print(*i)