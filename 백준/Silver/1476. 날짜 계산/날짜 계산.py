import sys
e1,s1,m1 = map(int,sys.stdin.readline().split())
year = 1
e = 1
s = 1
m = 1
while True:
    if e == e1 and s == s1 and m1 == m:
        break
    year+=1
    e+=1
    if e>=16: e=1
    s+=1
    if s>=29: s=1
    m+=1
    if m>=20: m=1
    
print(year)