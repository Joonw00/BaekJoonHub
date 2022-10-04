s = input()
s = int(s)
i = 0
tot = 0
while 1:
    i+=1
    tot+=i
    if tot>s:
        print(i-1)
        break
    if tot == s:
        print(i)
        break