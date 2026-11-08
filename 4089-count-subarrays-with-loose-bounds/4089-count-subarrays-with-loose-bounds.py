class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        
        last_invalid = None
        ans = 0
        
        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                last_invalid = i

            if last_invalid is None:
                ans += i + 1
            else:
                ans += i - last_invalid

        return ans