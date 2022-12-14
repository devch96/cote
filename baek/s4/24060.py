#알고리즘 수업 - 병합 정렬 1
import sys
input = sys.stdin.readline
ans = []
def merge_sort(list):
    if len(list) == 1:
        return list
    mid = (len(list)+1)//2
    left = merge_sort(list[:mid])
    right = merge_sort(list[mid:])
    i,j = 0,0
    temp = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            ans.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            ans.append(right[j])
            j+=1
    while i < len(left):
        temp.append(left[i])
        ans.append(left[i])
        i+=1
    while j < len(right):
        temp.append(right[j])
        ans.append(right[j])
        j+=1
    return temp
n,k = map(int,input().split())
numlist = list(map(int,input().split()))
merge_sort(numlist)
print(ans[k-1] if len(ans) >= k else -1)

        