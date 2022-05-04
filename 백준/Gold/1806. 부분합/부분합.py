import sys
n,s = map(int,sys.stdin.readline().split())
seq = list(map(int,sys.stdin.readline().split()))
f = l = 0
ans = 1
an = []
tot = seq[0]
#처음 부분 예외 처리
while True:
  if tot >= s or l == n-1:
    if tot>=s:
      an.append(ans)
    if ans == 1:
      break
    ans-=1
    tot-=seq[f]
    f+=1
  else:
    l+=1
    ans+=1
    tot+=seq[l]
  if f > n-1:
    break
if len(an) == 0:
  print(0)
else:
  print(min(an))