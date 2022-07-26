n = input()
num = [0] * 10
for i in range(len(n)):
    num[int(n[i])] += 1
num[6] += num[9]
if num[6]%2 == 1:
    num[6]+=1
num[6] //= 2
num[9] = 0
print(max(num))