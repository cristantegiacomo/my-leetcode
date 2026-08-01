class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0
        m2 = nums1[0] if len1>0 else nums2[0]
        rng = (len1+len2) // 2 + 1

        for _ in range(rng):
            m1 = m2
            if i < len1 and j < len2:
                if nums1[i] <= nums2[j]:
                    m2=nums1[i]
                    i+=1
                else:
                    m2=nums2[j]
                    j+=1
            elif j < len2:
                m2=nums2[j]
                j+=1
            elif i < len1:
                m2=nums1[i]
                i+=1

        if (len1+len2) %2==0:
            return (m1+m2) / 2
        else:
            return m2