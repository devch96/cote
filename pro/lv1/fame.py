#명예의 전당 (1)
def solution(k,score):
    answer = []
    temp = []
    for i in score:
        temp.append(i)
        temp.sort()
        if len(temp) > k:
            del temp[0]
        answer.append(temp[0])
    return answer
print(solution(8,[10,100,20,150,1,100,200]))