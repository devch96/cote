def solution(polynomial):
    x = 0
    num = 0
    for i in polynomial.split(" "):
        if i.isdigit():
            num += int(i)
        if 'x' in i:
            if len(i) > 1:
                x += int(i[:-1])
            else:
                x += 1
    result = []
    if x > 0:
        if x == 1:
            result.append("x")
        else:
            result.append(str(x)+"x")
    if num != 0:
        result.append(str(num))
    answer = ' + '.join(result)
    return answer

