import sys
g = int(sys.stdin.readline())

sq = []
i = 1
while True:
    sq.append(i**2)
    if i**2 - (i-1)**2> g:
        break
    i += 1
f = 0
l = 1
cnt = 0
while True:
    if f == len(sq):
        break
    if sq[l] - sq[f] == g:
        print(l+1)
        cnt += 1
        f+=1
        l+=1
    elif sq[l] - sq[f] < g and l < len(sq)-1:
        l += 1
    else:
        f += 1
if cnt == 0:
    print(-1)