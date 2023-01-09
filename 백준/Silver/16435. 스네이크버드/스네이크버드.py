import sys
n,l = map(int,sys.stdin.readline().split())
h = list(map(int,sys.stdin.readline().split()))
h.sort()
while(h and h[0]<=l):
    l+=1
    h.pop(0)
print(l)