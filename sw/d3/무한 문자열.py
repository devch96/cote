T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    s, t = input().split()
    for i in range(max(len(s),len(t)), (len(s)*len(t))+1):
        if i%len(s) == 0 and i % len(t) == 0:
            fs = s*(i//len(s))
            ft = t*(i//len(t))
            break
          
    if fs==ft:
        answer = "yes"
    else:
        answer = "no"
    print(f'#{test_case} {answer}')