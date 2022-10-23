def solution(lottos, win_nums):
    min_win = len(set([i for i in lottos if i != 0])&set(win_nums))
    max_win = min_win + lottos.count(0)
    def rank(n):
        if n == 6:
            return 1
        elif n == 5:
            return 2
        elif n == 4:
            return 3
        elif n == 3:
            return 4
        elif n == 2:
            return 5
        else:
            return 6
    return [rank(max_win), rank(min_win)]

"""
rank = [6,6,5,4,3,2,1]
"""
