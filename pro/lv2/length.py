#방문 길이
def solution(dirs):
    dir = [[0,1],[0,-1],[1,0],[-1,0]]
    visited=[]
    now = [0,0]
    for s in dirs:
        if s == "U":
            a = 0
        elif s == "D":
            a = 1
        elif s == "R":
            a = 2
        else:
            a = 3
        dx,dy = dir[a]
        if (now[0]+dx >= -5 and now[0]+dx <= 5) and (now[1]+dy >= -5 and now[1]+dy <= 5):
            visited.append((now[0],now[1],now[0]+dx,now[1]+dy))
            visited.append((now[0]+dx,now[1]+dy,now[0],now[1]))
            now[0] += dx
            now[1] += dy
    return len(set(visited))//2
print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))