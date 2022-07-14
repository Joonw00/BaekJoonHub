n = input()
n = int(n)
dp = []
i = 0
while len(dp) != 10001:
    i+=1
    temp = list(str(i))
    cnt = 0
    dev = 0
    for j in temp:
        if j!='6':
            cnt = 0
        else:
            cnt+=1
        if cnt == 3:
            dev = 1
            break
    if dev ==1:
        dp.append(i)
print(dp[n-1])