class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        sum_peak = sum_valley = 0
        for i in range(1, len(nums)-1):
            if nums[i] < nums[i-1] and nums[i] < nums[i+1]:
                sum_valley += nums[i]
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                sum_peak += nums[i]

        return sum_peak - sum_valley
            
            
            