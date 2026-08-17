class Solution:
    def strStr(self, haystack: str, needle: str) -> int:   
        size = len(needle)
        l = 0

        for r in range(size-1, len(haystack)):
            if haystack[l:r+1] == needle:
                return l
            l += 1

        return -1