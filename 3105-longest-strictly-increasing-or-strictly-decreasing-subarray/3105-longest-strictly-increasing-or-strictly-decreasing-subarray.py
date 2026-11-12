class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = asc = desc = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                asc += 1
                desc = 1
            elif nums[i] < nums[i-1]:
                desc += 1
                asc = 1
            else:
                asc = desc = 1

            ans = max(ans, asc, desc)
            
        return ans