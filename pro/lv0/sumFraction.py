def solution(denum1, num1, denum2, num2):
    def GCD(x,y):
        while(y):
            x,y = y, x%y
        return x

    def LCM(x,y):
        return x*y // GCD(x,y)


    denum = denum1 * num2 + denum2 * num1
    num = num1*num2
    return [denum//GCD(denum,num), num//GCD(denum,num)]

"""
import fractions
def solution(denum1, num1, denum2, num2):
    a = fractions.Fraction(denum1, num1) + fractions.Fraction(denum2, num2)
    answer = [a.numerator, a.denominator]
    return answer
"""

    
