def solution(park, routes):
    dir = {'E':[0,1],'W':[0,-1],'N':[-1,0],'S':[1,0]}
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                answer = [i,j]
    for route in routes:
        flag = True
        direction = dir.get(route.split()[0])
        num = int(route.split()[1])
        temp = answer
        if ((answer[0] + (direction[0] * num)) > i) or ((answer[1] + (direction[1] * num)) > j) or ((answer[0] + (direction[0] * num)) < 0) or ((answer[1] + (direction[1] * num)) < 0):
            continue
        for k in range(num):
            x,y = [x+y for x,y in zip(temp, direction)]
            if park[x][y] == 'X':
                flag = False
                break
            temp = [x,y]
        if flag:
            answer = temp
    return answer
print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))