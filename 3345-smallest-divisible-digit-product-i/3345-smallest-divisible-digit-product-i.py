class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
          # cent = n // 100
            dec = (n % 100) // 10
            unit = (n % 100) % 10
            if dec==0:
                if unit % t == 0:
                    return n
            elif (dec * unit) % t == 0:
                return n
            n+=1