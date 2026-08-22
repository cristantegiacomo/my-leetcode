class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        i = 1
        digSum = 0
        digProd = 1

        while num >= i:
            i *= 10
        i //= 10

        while i != 0:
            digSum += num // i 
            digProd *= num // i
            num = num % i
            i //= 10

        return True if (n % (digSum + digProd) == 0) else False