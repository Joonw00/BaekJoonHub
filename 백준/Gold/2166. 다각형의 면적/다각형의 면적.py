import sys
n = input()
n = int(n)
spot = []
for i in range(n):
  a,b = map(int,sys.stdin.readline().split())
  spot.append([a,b])

spot.append(spot[0])
p = 0
m = 0
for i in range(n):
  p+=spot[i][0]*spot[i+1][1]
  m+=spot[i][1]*spot[i+1][0]
ans = abs((p-m)*(1/2))
round(ans, 1)
print(ans)