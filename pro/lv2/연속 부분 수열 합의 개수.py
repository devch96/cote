def solution(elements):
    answer = set()
    for i in range(len(elements)):
        ssum = elements[i]
        answer.add(ssum)
        for j in range(i+1,i+len(elements)):
            ssum += elements[j%len(elements)]
            answer.add(ssum)
    return len(answer)
print(solution([7,9,1,1,4]))