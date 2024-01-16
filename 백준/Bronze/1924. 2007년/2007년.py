import sys
x,y = map(int,sys.stdin.readline().split())
tot = 0
if x == 1:
    tot = 0
elif x == 2:
    tot = 31
elif x == 3:
    tot = 59
elif x == 4:
    tot = 90
elif x == 5:
    tot = 120
elif x == 6:
    tot = 151
elif x == 7:
    tot = 181
elif x == 8:
    tot = 212
elif x == 9:
    tot = 243
elif x == 10:
    tot = 273
elif x == 11:
    tot = 304
elif x == 12:
    tot = 334
tot += y
if tot % 7 == 1:
    print("MON")
elif tot % 7 == 2:
    print("TUE")
elif tot % 7 == 3:
    print("WED")
elif tot % 7 == 4:
    print("THU")
elif tot % 7 == 5:
    print("FRI")
elif tot % 7 == 6:
    print("SAT")
elif tot % 7 == 0:
    print("SUN")