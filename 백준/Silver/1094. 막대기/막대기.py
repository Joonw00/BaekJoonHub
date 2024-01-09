import sys
n = int(sys.stdin.readline())
stick = 64
ans = 0
while 1:
    if stick == n:
        ans  += 1
        break
    elif stick > n:
        stick = stick /2 
    else:
        n = n - stick
        ans+=1
    if n == 0:
        break
print(ans)