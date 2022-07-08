n = input()
n = int(n)
ans = n
#에라토~ 체
for i in range(2,int(n**(1/2))+1):
    if n%i == 0:
        ans = ans * (1 - 1/i)
    while n%i == 0:
        n = n // i
#소수라면
if n>1:
    ans = ans* (1-1/n)
print(int(ans))