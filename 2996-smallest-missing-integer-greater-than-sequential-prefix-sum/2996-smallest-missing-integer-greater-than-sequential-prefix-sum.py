class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        somma = nums[0]
        seen = set(nums)

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] - 1:
                somma += nums[i+1]
            else:
                break
        
        while True:
            if somma not in seen:
                return somma
            else:
                somma += 1