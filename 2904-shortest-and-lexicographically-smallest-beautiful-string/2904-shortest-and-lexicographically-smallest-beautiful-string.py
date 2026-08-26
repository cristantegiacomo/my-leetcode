class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        arr = []
        l = 0
        lenn = float('inf')
        ones = 0

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
                tmp = lenn
                lenn = min(lenn, r-l+1)
                if r-l+1 == tmp:
                    arr.append(s[l:r+1])
                elif lenn < tmp:
                    arr.clear()
                    arr.append(s[l:r+1])

        if not arr:
            return ""

        res = arr[0]
        for i in range(1, len(arr)):
            res = min(res, arr[i])
        
        return res