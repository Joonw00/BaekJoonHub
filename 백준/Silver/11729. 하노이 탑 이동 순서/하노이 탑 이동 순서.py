def han(n,a,b,c):
    if n == 1:
        ans.append([a,c])
        return
    else:
        han(n-1,a,c,b)
        ans.append([a,c])
        han(n-1,b,a,c)
ans = []
a = input()
a = int(a)
han(a,1,2,3)
print(len(ans))
for i in ans:
    print(i[0],i[1])