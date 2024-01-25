def solution(progresses, speeds):
    answer = []
    dep = []
    l = len(speeds)
    for i in range(l):
        temp = int((100-progresses[i])/speeds[i])
        if (100-progresses[i])%speeds[i] != 0:
            temp += 1
        dep.append(temp)
    temp = 0
    s = 0
    for i in range(l):
        if temp < dep[i]:
            if i>0:
                answer.append(s)
            s = 1
            temp = dep[i]
        else:
            s+=1
    if s != 0:
        answer.append(s)
    return answer