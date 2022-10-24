def solution(numbers, hand):
    left = ["*"]
    right = ["#"]
    def distance(d1, d2):
        pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        for i in pad:
            if d1 in i:
                d1x = pad.index(i)
                d1y = i.index(d1)
            if d2 in i:
                d2x = pad.index(i)
                d2y = i.index(d2)
        return abs(d1x-d2x)+abs(d1y-d2y)
    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            numbers[numbers.index(x)] = 'L'
            left.append(x)
        elif x == 3 or x == 6 or x == 9:
            numbers[numbers.index(x)] = 'R'
            right.append(x)
        else:
            if distance(left[-1],x)>distance(right[-1],x):
                numbers[numbers.index(x)] = 'R'
                right.append(x)
            elif distance(left[-1],x)<distance(right[-1],x):
                numbers[numbers.index(x)] = 'L'
                left.append(x)
            else:
                if hand == "right":
                    numbers[numbers.index(x)] = 'R'
                    right.append(x)
                else:
                    numbers[numbers.index(x)] = 'L'
                    left.append(x)

    return ''.join(numbers)
print(solution([1,3,4,5,8,2,1,4,5,9,5],"right"))



