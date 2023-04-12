def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : (x*4)[:4], reverse=True)
    answer=''.join(numbers)
    return answer if answer[0] != '0' else '0'


print(solution([6,10,2]))
print(solution([3, 30, 34, 5, 9]))