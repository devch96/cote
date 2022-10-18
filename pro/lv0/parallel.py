def solution(dots):
    answer = 0
    def gradient(line):
        a , b = line
        x1, y1 = dots[a]
        x2, y2 = dots[b]
        if x1 == x2:
            return None
        else:
            return (y2-y1) / (x2-x1)
    for i in range(len(dots)):
        for j in range(i+1,len(dots)):
            line_1 = [i,j]
            line_2 = [x for x in range(len(dots)) if x not in line_1]
            if gradient(line_1) == gradient(line_2):
                answer = 1
    return answer
