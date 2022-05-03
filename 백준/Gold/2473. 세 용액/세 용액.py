import sys
N = input()
N = int(N)
liq = list(map(int,sys.stdin.readline().split()))
liq.sort()
m = 10**10
t = 0
for i in range(N-2):
  f = i+1
  l = N-1
  while f<l:
    sm = liq[i]+liq[f]+liq[l]
    if abs(sm) <=m:
      m = abs(sm)
      ans = [liq[i],liq[f],liq[l]]
    if sm<0:
      f+=1
    elif sm>0:
      l-=1
    else:
      t = 1
      break
  if t == 1:
    break
ans.sort()          
print(ans[0],ans[1],ans[2])