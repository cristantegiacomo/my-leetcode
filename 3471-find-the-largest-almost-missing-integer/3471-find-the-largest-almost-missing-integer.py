class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        seen = set()
        mp = {}
        
        if k != len(nums):
            for i, n in enumerate(nums):
                if n not in seen:
                    mp[n] = i
                    seen.add(n)
                else:
                    nums[i] = -1
                    nums[mp[n]] = -1
                    mp[n] = i


        if k == 1 or k == len(nums):
            return max(nums)
        elif k > 1:
            return max(nums[0], nums[-1])
