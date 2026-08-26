class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        ones = 0
        res = ""

        for r in range(len(s)):
            if s[r] == "1":
                ones += 1
            
            while ones > k and l < len(s):
                if s[l] == "1":
                    ones -= 1
                l += 1

            while l < len(s) and s[l] == "0":
                l += 1

            if ones == k:
                curr_len = r - l + 1

                if not res or curr_len < len(res):
                    res = s[l:r+1]
                elif curr_len == len(res):
                    res = min(res, s[l:r+1])

        return res