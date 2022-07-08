n = input()
n = int(n)
tot = 0
for j in range(1,n+1):
    j = int(j)
    ans = j
    #에라토~ 체
    for i in range(2,int(j**(1/2))+1):
        if j%i == 0:
            ans = ans * (1 - 1/i)
        while j%i == 0:
            j = j // i
    #소수라면
    if j>1:
        ans = ans* (1-1/j)
    tot+= int(ans)
print(tot-1) #1제외