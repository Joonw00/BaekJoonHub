import sys
n = input()
k = sys.stdin.readline().rstrip()
l = len(n)
while True:
  if k == n:
    print(1)
    break
  if l>len(k):
    print(0)
    break
  if k[-1] == 'A':
    k = k[:-1]
  elif k[-1] == 'B':
    k = k[-2::-1]