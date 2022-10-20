def solution(n):
    def ternary(x):
        temp = ''
        while x > 0:
            x, r = divmod(x,3)
            temp += str(r)
        return temp[::-1]
    return int(ternary(n)[::-1],3)
