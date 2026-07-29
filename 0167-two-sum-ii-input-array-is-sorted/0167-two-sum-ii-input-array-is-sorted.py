class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            somma = numbers[l] + numbers[r]
            
            if somma > target:
                r -= 1
            elif somma < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []        