import sys
N = input()
N = int(N)
liq = list(map(int,sys.stdin.readline().split()))

f = 0
l = N-1
ans = []

while f<l:
  ans.append([abs(liq[f]+liq[l]), f, l])
  if abs(liq[f])>abs(liq[l]):
    f+=1
  elif abs(liq[f])<abs(liq[l]):
    l-=1
  elif abs(liq[f])==abs(liq[l]):
    break
a = min(ans)
print("{0} {1}".format(liq[a[1]],liq[a[2]]))