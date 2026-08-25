class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        res = 0

        def dfs(i):
            maximum = 0
            if i >= len(nums):
                return 0

            if cache[i] != -1:
                return cache[i]

            for j in range(i+2, len(nums)):
                maximum = max(maximum, dfs(j))
            cache[i] = nums[i] + maximum

            return cache[i]
        
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res