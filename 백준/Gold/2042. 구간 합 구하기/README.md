  # 이거 왜 틀림????

  import sys

  import math

  global ans

  def change_num(idx,c):
    dt = c - seg[idx]
    while idx != 0:
      seg[idx] += dt
      idx = (idx-1)//2
    seg[0]+=dt
  #2번 연산
  def sum_range(search_f,search_l,idx_f,idx_l,idx):
    global ans
    mid = (idx_f + idx_l)//2
    if search_f<=idx_f and search_l>=idx_l:
      ans+=seg[idx]
      return
    if mid >= search_f: #좌측 노드로
      sum_range(search_f,search_l,idx_f,mid,idx*2+1)
    if mid < search_l: #우측 노드로
      sum_range(search_f,search_l,mid+1,idx_l,idx*2 + 2)


  N,M,K = map(int,sys.stdin.readline().split())
  n = math.ceil(math.log2(N))
  size = 2**n
  tot_size = size
  #세그먼트 초기화
  seg = [0] * (size*2-1)
  for i in range(N):
    temp = sys.stdin.readline().rstrip()
    temp = int(temp)
    seg[size-1 + i] = temp
  #size-1:왼끝
  while size // 2 != 0:
    size = size//2
    for i in range(size-1,size*2 -1):
      seg[i] = seg[2*i + 1]+seg[2*i + 2]

  #idx0 따로 처리
  if N == 1:
    seg[0] = seg[1]
  else:
    seg[0] = seg[1]+seg[2]
  for i in range(M+K):
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1:
      change_num(tot_size - 2 + b,c)
    elif a == 2:
      ans = 0
      sum_range(tot_size - 2 + b, tot_size - 2 + c,tot_size-1,tot_size*2 - 2,0)
      print(ans)
