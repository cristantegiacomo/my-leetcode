class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]

        for i in range(len(nums)-2):
            l, r = i+1, len(nums) - 1
            if i > 0 and nums[i]==nums[i-1]: continue

            while l<r:
                somma=nums[l]+nums[r]
                if somma > -nums[i]:
                    r-=1
                elif somma < -nums[i]:
                    l+=1
                else:
                    res.append( [nums[i], nums[l], nums[r]] )
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return res        