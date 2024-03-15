def solution(n, control):
    answer = n
    for i in range(len(control)):
        if control[i] == "w":
            answer+=1
        if control[i] == "s":
            answer-=1
        if control[i] == "d":
            answer+=10
        if control[i] == "a":
            answer-=10
    return answer