class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        
        for a1 in arr1:
            found = False
            for a2 in arr2:
                if abs(a2 - a1) <= d:
                    found = True
                    break
            if not found:
                ans += 1
        
        return ans