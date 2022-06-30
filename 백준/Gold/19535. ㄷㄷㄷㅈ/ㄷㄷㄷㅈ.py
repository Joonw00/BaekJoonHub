import copy
import sys
n = input()
n = int(n)
t = []
nd = [0]*(n+1)
for _ in range(n-1):
    u,v = map(int,sys.stdin.readline().split())
    nd[u]+=1
    nd[v]+=1 
    t.append([u,v])

#ㅈ개
jsum = 0
for i in range(1,n+1):    
    i = int(i)
    if nd[i]>=3:
        jsum+= nd[i]*(nd[i]-1)*(nd[i]-2) / 6

#ㄷ개수
dsum = 0
for a,b in t:
    if nd[a]>1 and nd[b]>1:
        dsum+=(nd[a]-1) * (nd[b]-1)
    
if dsum>jsum*3:
    print("D")
elif dsum<jsum*3:
    print("G")
else:
    print("DUDUDUNGA")