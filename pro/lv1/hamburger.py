def solution(ingredient):
    temp = ''.join(map(str,ingredient))
    answer = 0
    idx = 0
    while idx < len(temp)-3 :
        if temp[idx] == '1':
            if temp[idx:idx+4] == '1231':
                temp = temp[:idx]+temp[idx+4:]
                idx -= 3
                answer += 1
                continue
        idx+=1
    return answer
print(solution([2,1,1,2,3,1,2,3,1]))
print(solution([1,3,2,1,2,1,3,1,2]))