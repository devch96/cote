#너의 평점은
import sys
input = sys.stdin.readline
scoreTable = {"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}
totalScore = 0
totalCredit = 0
for _ in range(20):
    subject, credit, score = input().split()
    if score != 'P':
        totalScore += scoreTable[score] * int(credit[0])
        totalCredit += int(credit[0])
print(totalScore/totalCredit)
