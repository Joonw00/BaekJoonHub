import sys

x,y = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
B = list(map(int,sys.stdin.readline().split()))
#둘 중 1개의 집합에만 포함된 개수 선택
As = set(A)
A = list(As)
Bs = set(B)
B = list(Bs) #중복 제거
A.sort()
B.sort()
a = 0
b = 0 #인덱스
ctn = 0
x = len(A)
y = len(B)
while True:
  if x == a or y == b:
    break
  if A[a] ==B[b]:
    a+=1
    b+=1
    ctn+=1
  elif A[a] > B[b]:
    b+=1
  elif A[a] < B[b]:
    a+=1
print(x+y - 2*ctn)