import sys
T =  input()
T = int(T)

for _ in range(T):
    n = sys.stdin.readline()
    n = int(n)
    if n==0:
        print(0)
        continue
    Wear = []
    for i in range(n):
        a,b = sys.stdin.readline().split()
        Wear.append(b)
    Wear.sort()
    cnt = []
    cnt.append(2)
    for i in range(1,n):   #범위 확인
        if Wear[i] != Wear[i-1]:    #다르면 새로운 cnt에
            cnt.append(2)
        if Wear[i] == Wear[i-1]:
            cnt[len(cnt)-1] += 1
    ans = 1
    l = len(cnt)
    for i in range(l):
        ans=ans*cnt[i]
    print(ans-1)