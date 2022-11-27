n = int(input())
k = 0
while True:
    if n%5 == 0:
        k += n//5
        print(k)
        break
    n -= 2
    k += 1
    if n < 0:
        print(-1)
        break
    
