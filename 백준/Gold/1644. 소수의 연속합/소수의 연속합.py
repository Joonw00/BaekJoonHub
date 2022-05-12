import sys
n = input()
n = int(n)
era = [True]*(n+1) # True : 소수, False : 소수x
era[1] = False
era[0] = False
for i in range(2,n):
  i = int(i)
  if era[i] == False:
    continue
  temp = i * 2
  while temp <= n:
    era[temp] = False
    temp += i
#소수
dec = []
for i in range(1,n+1):
  i = int(i)
  if era[i]:
    dec.append(i)
ans = 0
s = 0
e = 0

l = len(dec)
if l != 0:
  tot = dec[0]
  while s<=e:
    if tot == n:
      ans+=1
      if e<l-1:
        e+=1
        tot+=dec[e]
      else:
        break
    elif tot < n:
      if e<l-1:        
        e+=1
        tot+=dec[e]
      else:
        break
    elif tot>n:
      tot-=dec[s]
      s+=1

print(ans)