def solution(sides):
    """
    max(sides)가 가장 긴 변일 경우
    sum(sides) - max(sides) + i > max(sides)

    sum(sides) + i > 2 * max(sides)
    
    i > 2*max(sides)-sum(sides)


    i가 가장 긴 변일경우
    sum(sides) > i

    sum(sides)-i>0

    i<sum(sides)
    """

    return 2*(sum(sides)-max(sides)) -1

    
