k = int(input())
btn = []
btn.append([1,0])
for i in range(45):
    b = btn[i][0] + btn[i][1]
    a = btn[i][1]
    btn.append([a,b])
print(btn[k][0], btn[k][1])