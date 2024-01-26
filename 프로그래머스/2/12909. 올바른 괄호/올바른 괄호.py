def solution(s):
    answer = True
    l = len(s)
    temp = 0
    for i in range(l):
        if s[i] =="(":
            temp += 1
        else:
            temp -= 1
            if temp < 0:
                answer = False
    if temp != 0:
        answer = False
    
    return answer