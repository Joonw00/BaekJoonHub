import sys
N = input()
N = int(N)
kg = []
for i in range(N):
    a = sys.stdin.readline().rstrip()
    a = int(a)
    kg.append(a)
kg.sort()
sum = 0
ans = []
sav = kg[len(kg)-1]
for i in range(len(kg)-1,-1,-1):   
    i = int(i)
    small = kg[i]
    #이전 무게와 같으면 continue
    if small == sav:
        sum+=1
        continue
    else:
        ans.append(sum*sav)
        sum+=1
        sav = small
ans.append(sum*sav)
print(max(ans))