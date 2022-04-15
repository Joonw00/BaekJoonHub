import sys
p = []
for i in range(3):
  a,b = map(int,sys.stdin.readline().split())
  p.append([a,b])
dx1 = p[1][0] - p[0][0]
dy1 = p[1][1] - p[0][1]
dx2 = p[2][0] - p[1][0]
dy2 = p[2][1] - p[1][1]

#일직선
if dy1*dx2 == dy2*dx1:
  print(0)
else:
  #x=1그래프 생각
  if p[0][0] > p[1][0]:
    if p[0][1]*dx1 + (p[2][0]-p[0][0]) * dy1 < dx1*p[2][1]:
      print(1)
    else:
      print(-1)
  elif p[0][0] < p[1][0]:
    if p[0][1]*dx1 + (p[2][0]-p[0][0]) * dy1 > dx1*p[2][1]:
      print(-1)
    else:
      print(1)
  else:
    if p[0][1] > p[1][1]:
      if p[2][0] > p[1][0]:
        print(1)
      else:
        print(-1)

    else:
      if p[2][0] > p[1][0]:
        print(-1)
      else:
        print(1)