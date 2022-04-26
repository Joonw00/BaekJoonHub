N = input()
N = int(N)

ans = [0]*(N+1)
ans[1] = -1
ans[2] = -1
a = 1
b = 2
fibo = []
fibo.append(1)
fibo.append(2)

while a+b <= N:
  ans[a+b] = -1
  fibo.append(a+b)
  temp = b
  b = a+b
  a = temp
n = N
if n in fibo:
  print(-1)
else:
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
