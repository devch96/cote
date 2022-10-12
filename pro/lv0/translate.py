def solution(rsp):
    answer = rsp.translate(str.maketrans({"2":"0","0":"5","5":"2"}))
    return answer
