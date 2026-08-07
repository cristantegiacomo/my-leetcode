class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            dec = (n // 10) % 10
            unit = n % 10
            if n < 10:
                if unit % t == 0:
                    return n
            elif n == 100:
                return 100
            elif (dec * unit) % t == 0:
                return n
            n+=1