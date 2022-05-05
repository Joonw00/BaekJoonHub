import sys
def fnd(x):
  if x!=par[x]:
    par[x] = fnd(par[x])
  return par[x]

v,e = map(int,sys.stdin.readline().split())
par = []
for i in range(v+1):
  par.append(i)
line = []
for i in range(e):
  a,b,c = map(int,sys.stdin.readline().split())
  line.append([c,a,b])
line.sort()

ans  = 0
#모든 간선들에 대하여
for i in range(e):
  s = fnd(line[i][1])
  e = fnd(line[i][2])
  cost = line[i][0]
  #처음과 같지 않다면 연결
  if s != e:
    par[s] = e
    ans += cost
print(ans)
