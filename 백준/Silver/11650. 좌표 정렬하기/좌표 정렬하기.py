import sys

n = input()
n = int(n)
coor = []
for _ in range(n):
  x,y = map(int,sys.stdin.readline().split())
  coor.append([x,y])
coor.sort(key = lambda x : x[1])
coor.sort()
for i in range(n):
  print(coor[i][0], coor[i][1])
