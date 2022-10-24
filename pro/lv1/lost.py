def solution(n, lost, reserve):
    com = set(lost) & set(reserve)
    lost = sorted(list(set(lost) - com))
    reserve = sorted(list(set(reserve) - com))

    for i in lost[:]:
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)
    return n - len(lost)

