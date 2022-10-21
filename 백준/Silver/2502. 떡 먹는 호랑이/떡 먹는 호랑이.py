import sys
a,b = map(int,sys.stdin.readline().split())
temp = b
fib=[1,2]
for i in range(a):
    fib.append(fib[i]+fib[i+1])
if a == 3:
    print(1)
    print(b-1)
else:
    ans = 0
    for i in range(1,100000):
        for j in range(i+1,100000):
            temp = fib[a-4]*i+fib[a-3]*j
            if temp == b:
                print(i)
                print(j)
                ans = 1
                break
        if ans == 1:
            break