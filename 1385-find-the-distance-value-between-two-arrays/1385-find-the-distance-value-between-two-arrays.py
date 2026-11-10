class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        # N = len(arr2), M = len(arr1)
        ans = 0
        arr2.sort() # NlogN

        def find_close(x): #logN
            l, r = 0, len(arr2)-1
            while l <= r:
                m = l + (r-l) // 2
                if abs(x - arr2[m]) <= d:    # if not far
                    return True
                else:
                    if arr2[m] > x:
                        r = m - 1
                    else:
                        l = m + 1
            return False

        for x in arr1: #MlogN
            if not find_close(x): # se sono tutti far
                ans += 1
        
        return ans
