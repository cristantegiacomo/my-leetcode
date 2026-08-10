class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        k = 1
        for i in range(len(word)):
            if i != 0 and i % 8 == 0: k+= 1
            res += k
        return res