class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        seen1 = set(nums1)
        seen2 = set(nums2)
        answer = [ [] for _ in range(2) ]

        for n in seen1:
            if n not in seen2:
                answer[0].append(n)

        for n in seen2:
            if n not in seen1:
                answer[1].append(n)
                
        return answer