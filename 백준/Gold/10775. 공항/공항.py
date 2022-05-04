import sys
def fnd(idx):
  if idx != port[idx]:
    port[idx] = fnd(port[idx])
  return port[idx]
g = input()
p = input()
g = int(g)
p = int(p)
#몇 번 포트 이하로 들어가야 하는 지
gport = []
for i in range(p):
  a = sys.stdin.readline().rstrip()
  a = int(a)
  gport.append(a)
ans = 0

#역추적
port = []
for i in range(g+1):
  port.append(i)
for i in gport:
  idx = fnd(i)
  if idx == 0:
    break

  port[idx] = fnd(idx-1) 
  port[i] = port[idx]
  ans+=1
print(ans)