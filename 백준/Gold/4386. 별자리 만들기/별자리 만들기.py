import sys
import math
def ufind(x):
  if x!=uni[x]:
    uni[x] = ufind(uni[x])
  return uni[x]

n = input()
n = int(n)
uni = [i for i in range(n+1)]
star = []
for i in range(n):
  a,b = map(float,sys.stdin.readline().split())
  star.append([a,b])
leng = []
for i in range(n-1):
  for j in range(i+1,n):
    l = math.sqrt((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)
    leng.append([l,i,j])
leng.sort()
ans = 0
for cost,a,b in leng:
  s = ufind(a)
  e = ufind(b)
  #다른 지역이라면
  if s!=e:
    if s<e:
      uni[e] = s
    else:
      uni[s] = e  
    ans+=cost
ans = round(ans, 2)
print(ans)