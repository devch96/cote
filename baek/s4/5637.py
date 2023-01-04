#가장 긴 단어
import re
arr = re.findall('[A-Z\-a-z]+', open(0).read()[:-1])
arr.sort(key=lambda x: len(x), reverse=True)
print(arr[0].lower())