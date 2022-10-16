def solution(num, total):
    x = (total - (num*(num-1)//2))//num
    answer = [i for i in range(x,x+num)]
    return answer
