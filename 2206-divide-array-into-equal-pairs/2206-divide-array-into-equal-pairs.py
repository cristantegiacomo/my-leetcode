class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        counts = Counter(nums)

        for c, freq in counts.items():
            if freq%2 != 0:
                return False
        return True