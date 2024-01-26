def solution(s):
    answer = ''
    sp = s.split(" ")
    for i in range(len(sp)):
        sp[i] = int(sp[i])
    sp.sort()
    a = str(sp[0])
    b = str(sp[-1])
    answer = a+" "+b
    return answer