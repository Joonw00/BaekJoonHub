n = input()
n = list(n)
n.sort(reverse=True)
sm = 0
for i in range(len(n)):
    sm+=int(n[i])
if '0' in n and sm%3==0:
    for i in n:
        print(i,end='')
else:
    print(-1)