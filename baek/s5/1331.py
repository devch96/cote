from sys import stdin
input = stdin.readline
visited = [input().rstrip() for i in range(36)]
def X(x1,x2):
    return abs(ord(visited[x1][0]) - ord(visited[x2][0]))

def Y(y1,y2):
    return abs(int(visited[y1][1]) - int(visited[y2][1]))
answer = "Valid"
if len(set(visited)) != 36:
    answer = "Invalid"
if not ((X(0,-1) == 2 and Y(0,-1) == 1) or (X(0,-1) == 1 and Y(0,-1) == 2)):
    answer = "Invalid"
for i in range(35):
        if not ((X(i,i+1) == 2 and Y(i,i+1) == 1) or (X(i,i+1) == 1 and Y(i,i+1) == 2)):
            answer = "Invalid"
print(answer)