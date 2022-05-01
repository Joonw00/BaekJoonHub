import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
def mv_l(y,x):
  for i in range(1,9):
    i = int(i)
    if toy[y][x-i] == 'O':
      return [y,x-i]
    if toy[y][x-i] == '#':
      return [y,x-i+1]

def mv_r(y,x):
  for i in range(1,9):
    i = int(i)
    if toy[y][x+i] == 'O':
      return [y,x+i]
    if toy[y][x+i] == '#':
      return [y,x+i-1]
def mv_u(y,x):
  for i in range(1,9):
    i = int(i)
    if toy[y-i][x] == 'O':
      return [y-i,x]
    if toy[y-i][x] == '#':
      return [y-i+1,x]
def mv_d(y,x):
  for i in range(1,9):
    i = int(i)
    if toy[y+i][x] == 'O':
      return [y+i,x]
    if toy[y+i][x] == '#':
      return [y+i-1,x]


toy = []
for i in range(N):
  toy.append(sys.stdin.readline().rstrip())
for i in range(N):
  for j in range(M):
    if toy[i][j] == 'B':
      b_pos = [i,j]

    if toy[i][j] == 'R':
      r_pos = [i,j]
    
    if toy[i][j] == 'O':
      o_pos = [i,j]

BR = deque()
BR.append([b_pos,r_pos,1])

#o를 지나가면 해당 좌표값 반환!
#예외처리 : 같은 줄에서 움질이면 겹치지 못한다
while BR:
  b,r,n = BR.popleft()
  if n == 11:
    print(-1)
    break
  #왼쪽
  bl = mv_l(b[0],b[1])
  rl = mv_l(r[0],r[1])
  if rl == o_pos:
    if rl == bl:
      pass
    else:
      print(n)
      break
  if bl != o_pos:
    if rl[0] == bl[0] and bl[1] == rl[1]:
      if b[1]<r[1]:
        rl[1]+=1
      else:
        bl[1]+=1
    BR.append([bl,rl,n+1])

  #오른쪽
  br = mv_r(b[0],b[1])
  rr = mv_r(r[0],r[1])
  #둘 다 O를 지난다면?
  if rr == o_pos:
    if rr == br:
      pass
    else:
      print(n)
      break
  if br != o_pos:
    if rr[0] == br[0] and br[1] == rr[1]:
      if b[1]<r[1]:
        br[1]-=1
      else:
        rr[1]-=1
    BR.append([br,rr,n+1])
  
  #위로
  bu = mv_u(b[0],b[1])
  ru = mv_u(r[0],r[1])
  if ru == o_pos:
    if ru == bu:
      pass
    else:
      print(n)
      break
  if bu != o_pos:
    if ru[0] == bu[0] and bu[1] == ru[1]:
      if b[0]<r[0]:
        ru[0]+=1
      else:
        bu[0]+=1
    BR.append([bu,ru,n+1])

  #아래
  bd = mv_d(b[0],b[1])
  rd = mv_d(r[0],r[1])
  if rd == o_pos:
    if rd == bd:
      pass
    else:
      print(n)
      break
  if bd != o_pos:
    if rd[0] == bd[0] and bd[1] == rd[1]:
      if b[0]<r[0]:
        bd[0]-=1
      else:
        rd[0]-=1
    BR.append([bd,rd,n+1])