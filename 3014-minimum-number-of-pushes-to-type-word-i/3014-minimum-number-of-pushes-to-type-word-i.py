class Solution:
    def minimumPushes(self, word: str) -> int:
        lung = len(word)
        giri = lung // 8
        resto = lung % 8
        somma = i = 0

        for i in range(giri):
            somma = somma + i + 1

        return 8*somma + (giri+1)*resto