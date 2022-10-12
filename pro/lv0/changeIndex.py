def solution(my_string, num1, num2):
    x = my_string[num1]
    y = my_string[num2]
    temp = list(my_string)
    temp[num1] = y
    temp[num2] = x
    answer = ''.join(temp)
    return answer
