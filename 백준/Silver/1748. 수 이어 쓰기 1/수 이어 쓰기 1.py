import sys
n = input()
n = int(n)
n1 = n
c = 0 #자릿수
while n1:
  c+=1
  n1 = n1//10

if c == 1:
  print(n)
else:
  left = n - 10**(c-1) + 1
  count = 0
  count+=left*c
  c-=1
  while c:
    temp = 10**c - 10**(c-1)
    count+=temp * c
    c-=1
  print(count)