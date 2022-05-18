import sys
import math
  
def fmin(node,s,e):
  l = min_seg[node][1]
  r = min_seg[node][2]
  if s>r or e<l:
    return 10**10
  if s<=l and e>=r:
    return min_seg[node][0]
  return min(fmin(node*2+1,s,e),fmin(node*2 + 2, s,e))

n,m = map(int,sys.stdin.readline().split())
h = 1+math.ceil(math.log2(n))
t_size = 2**h
min_seg = [10**10]*(t_size-1)

for i in range(2**(h-1)):
  idx = 2**(h-1) - 1 + i
  if i<n:
    a = sys.stdin.readline().rstrip()
    a = int(a)
    #idx1부터idx2까지의 최대,소는 a이다.
    min_seg[idx] = [a,idx,idx]
  else:
    min_seg[idx] = [10**10,idx,idx]
#세그먼트 생성
temp = h
while temp-1:
  s = 2**(temp-1) - 1
  e = 2**temp - 2
  for i in range(s,e+1,2):
    min_seg[i//2] = [min(min_seg[i][0],min_seg[i+1][0]),min_seg[i][1],min_seg[i+1][2]]
  temp-=1

for _ in range(m):
  s,e = map(int,sys.stdin.readline().split())
  s += 2**(h-1)-2
  e += 2**(h-1)-2
  print(fmin(0,s,e))