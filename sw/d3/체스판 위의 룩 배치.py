T = int(input())
for test_case in range(1,T+1):
    table = [input() for s in range(8)]
    y = []
    flag = False
    for i in range(8):
        if table[i].count('O') > 1:
            print(f'#{test_case} no')
            flag = True
            break
        if table[i].index('O') in y:
            print(f'#{test_case} no')
            flag = True
            break
        y.append(table[i].index('O'))
    if not flag:
        print(f'#{test_case} yes')