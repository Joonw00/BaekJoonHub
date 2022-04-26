N = input()
N = int(N)

a = 1
b = 2
fibo = []
fibo.append(1)
fibo.append(2)

while a+b <= N:
  fibo.append(a+b)
  temp = b
  b = a+b
  a = temp
n = N
while True:
  l = fibo.pop()
  if l>n:
    l = fibo.pop()
  idx = n-l
  if idx == 0:
    print(n)
    break
  m = fibo[-1]
  f = fibo[-2]
  if idx <= l-m-1:
    n = m+idx
  else:
    n = f+idx-l+m
