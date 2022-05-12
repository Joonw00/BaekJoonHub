import sys
n = input()
c = len(n)
n = int(n)

left = n - 10**(c-1) + 1
count=left*c
c-=1
while c:
  temp = 10**c - 10**(c-1)
  count+=temp * c
  c-=1
print(count)