def solution(k, tangerine):
    answer = 0
    counter = {}
    for value in tangerine:
        try: counter[value] += 1
        except: counter[value] = 1
    counter = list(counter.values())
    counter.sort(reverse = True)
    tot = 0
    for i in counter:
        if tot + i > k:
            answer+=1
            break
        elif tot + i< k:
            answer += 1
            tot+=i
        else:
            answer+=1
            break
            
    return answer