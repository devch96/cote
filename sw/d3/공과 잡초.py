T = int(input())
for test_case in range(1,T+1):
    field = input()
    print(f'#{test_case} {field.count("(") + field.count(")") - field.count("()")}')