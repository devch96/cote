def solution(my_string):
    answer = [int(x) for x in my_string if x.isdigit()]
    answer.sort()
    return answer


