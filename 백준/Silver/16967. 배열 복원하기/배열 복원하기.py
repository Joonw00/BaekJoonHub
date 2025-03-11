import sys

h,w,x,y = map(int,sys.stdin.readline().split())

graph = []
for i in range(h+x):
    graph.append(list(map(int,sys.stdin.readline().split())))


A = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        A[i][j] = graph[i][j]


for i in range(x,h):
    for j in range(y,w):
        A[i][j] -= A[i-x][j-y]


for i in range(h):
    for j in range(w):
        print(A[i][j],end=' ')
    print()