from sys import stdin
_ = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
_ = stdin.readline()
M = list(map(int,stdin.readline().split()))

def binary(n, N, start, end):
    if start > end:
        return 0
    m = start + ((end-start)//2)
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)
dic = {}
for i in N:
    start = 0
    end = len(N) -1
    if i not in dic:
        dic[i] = binary(i,N,start,end)
print(' '.join(str(dic[x]) if x in dic else '0' for x in M))