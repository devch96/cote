T = int(input())
for test_case in range(1,T+1):
    A,B = map(int,input().split())
    M = int(('1'*A)+('0'*B),2)
    m = int('1' + ('0'*B) + ('1'*(A-1)),2)
    answer = bin(M*m).count('1')
    print(f'#{test_case} {answer}')
