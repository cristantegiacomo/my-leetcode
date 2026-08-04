class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        small = min(nums)
        big = max(nums)
        seen = set(nums)
        res = []

        for i in range(small, big):
            if i not in seen:
                res.append(i)
        return res
        