def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t) - l + 1):
        temp = t[i:i+l]
        temp = int(temp)
        if temp <= int(p):
            answer+=1
    return answer