def solution(name, yearning, photo):
    answer = []
    l = len(name)
    for i in range(len(photo)):
        temp = photo[i]
        tot = 0
        for n in temp: #photo에 있는 사람 이름
            for j in range(l):
                if n == name[j]:
                    tot +=yearning[j]
                    break
        answer.append(tot)
    return answer