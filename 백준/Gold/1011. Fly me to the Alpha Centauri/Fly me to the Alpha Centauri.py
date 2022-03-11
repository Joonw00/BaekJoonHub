import sys
T = input()
T = int(T)

for i in range(0,T):
    x,y = sys.stdin.readline().split()
    x = int(x)
    y = int(y)  
    l = y-x #사이 간격
    k = 0   #속도
    sum = 0     #이동한 거리
    i = 0       #이동 횟수
    if l ==2:
        print(2)
        continue
    while l-2*sum>k+1:
        k+=1
        sum +=k
        i +=1
    i = i*2 #올라가는 횟수==내려가는 횟수
    if sum>l/2: #k이동 1회만 함
        i-=1
        left = 1-2*sum +k
    else:
        left=l-2*sum

    if left == k:   #탈출 조건
        i+=1
    elif left == k-1:
        i+=1
    elif left< k and left!=0:
        i+=1
    elif left == k+1:
        i+=1
    elif left>k:
        a = left/k  #a는 꼭대기에서 k이동인횟수
        if left%k != 0:
            i += 1
        a = int(a)
        i +=a
    print(i)

  