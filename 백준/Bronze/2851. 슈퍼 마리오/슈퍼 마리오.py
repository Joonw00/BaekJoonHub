ans= [0]
for i in range(10):
    n = int(input())
    ans.append(ans[-1] + n)

score = 0
for i in range(1,11):
    if abs(score-100) >= abs(ans[i]-100):
        score = ans[i]
print(score)