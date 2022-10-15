def solution(keyinput, board):
    answer = [0,0]
    for i in keyinput:
        if i == "right":
            if answer[0] < (board[0]//2):
                answer[0] += 1
        elif i == "left":
            if answer[0] > (board[0]//2)*-1:
                answer[0] -= 1
        elif i == "up":
            if answer[1] < (board[1]//2):
                answer[1] += 1
        else:
            if answer[1] > (board[1]//2)*-1:
                answer[1] -= 1
    return answer
