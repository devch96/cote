def solution(X,Y):
    temp = ''
    for i in '9876543210':
        if i in X and i in Y:
            temp += i*min(X.count(i),Y.count(i))
    if len(temp) == 0:
        return "-1"
    elif len(temp) == temp.count('0'):
        return "0"
    else:
        return temp


