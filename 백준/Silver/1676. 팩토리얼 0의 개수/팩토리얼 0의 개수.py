import sys
N = input()
N = int(N)
sec = 0
fiv = 0
for i in range(1, N+1):
    i = int(i)
    while True:
        if i % 2 == 0:  #i가 2의 배수라면
            sec+=1
            i = i//2
        elif i%2 != 0:
            break
    while True:
        if i%5 == 0:
            fiv += 1
            i = i//5
        elif i%5 != 0:
            break
print(min(fiv, sec))