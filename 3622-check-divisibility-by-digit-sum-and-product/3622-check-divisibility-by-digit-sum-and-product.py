class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        digSum = 0
        digProd = 1

        while num > 0:
            digit = num % 10
            digSum += digit
            digProd *= digit
            num //= 10

        return n % (digSum + digProd) == 0