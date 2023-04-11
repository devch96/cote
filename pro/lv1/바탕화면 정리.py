def solution(wallpaper):
    answer = []
    up = []
    down = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                up.append([i,j])
                down.append([i+1,j+1])
    up = list(zip(*up))
    down = list(zip(*down))
    answer.append(min(up[0]))
    answer.append(min(up[1]))
    answer.append(max(down[0]))
    answer.append(max(down[1]))
    return answer
print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
print(solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]))