import re
n = int(input())
num_list = [str(i) for i in range(1,n+1)]
for i in range(n):
    num_list[i] = re.sub('3|6|9',"-",num_list[i])
    if '-' in num_list[i]:
        num_list[i] = num_list[i].count('-') * '-'
print(*num_list)