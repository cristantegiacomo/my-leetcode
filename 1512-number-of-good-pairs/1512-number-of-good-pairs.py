class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        res = 0

        for n in nums:
            res += counts[n]
            counts[n] += 1
        return res