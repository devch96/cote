T=int(input())
total = set()
for i in range(1, 10):
    for j in range(1,10):
        total.add(i*j)
for test_case in range(1,T+1):
    N = int(input())
    print(f'#{test_case} Yes' if N in total else f'#{test_case} No')