def solution(board, moves):
    board = list(zip(*board[::-1]))
    for a in range(len(board)):
        board[a] = list(filter(lambda x:x!=0, board[a]))
    count = 0
    bag = []
    for i in moves:
        if board[i-1]:
            cur = board[i-1].pop()
            bag.append(cur)
        if len(bag) > 1:
            if bag[-2] == bag[-1]:
                count += 1
                del bag[-2:]
    return count*2