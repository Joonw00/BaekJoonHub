import sys
A = input()
T = input()
T = list(T)
A = list(A)

ln = len(A)
#index
front = 0
last = len(T) - 1
f = []
l = []

#0:front 1:last
turn = 0

while front <= last:
  if turn == 0:
    f.append(T[front])
    front+=1
    if f[-ln:] == A[0:]:
      f[-ln:] = []
      turn = 1
  elif turn ==1:
    l.append(T[last])
    last-=1
    if l[-ln:] == A[-1: :-1]:
      l[-ln:] = []
      turn = 0

#합쳐진 이후에는 현 상태 마다 최대 1개의 검열 대상이 존재 가능
while l:
  f.append(l.pop())
  if f[-1:-1-ln:-1] == A[-1: :-1]:
    f[-ln:] = []


for i in f:
  print(i,end="")