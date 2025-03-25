import sys

n,score,p = map(int,sys.stdin.readline().split())
if n <= 0:
    print(1)
else:
    test = list(map(int,sys.stdin.readline().split()))

    test.sort(reverse=True)
    ans = n+1
    for i in range(n):
        if test[i] <= score:
            ans = i+1
            break
    if p == n and  test[-1] >= score:
        ans = -1
    print(ans)