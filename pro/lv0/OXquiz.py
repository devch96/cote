def solution(quiz):
    answer = []
    for i in quiz:
        temp = i.split()
        que = ''.join(temp[0:3])
        if eval(que) == int(temp[-1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

"""
def valid(equation):
    equation = equation.replace("=","==")
    return eval(equation)

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]

"""
