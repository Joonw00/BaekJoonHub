m = int(input())
n = int(input())
s = 0
mini = 0
for i in range(m, n+1):
    if i**0.5 == int(i**0.5):
        s += i
        if mini == 0:
            mini = i
if s == 0:
    print(-1)
else:
    print(s)
    print(mini)