class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        seen=set(nums)

        for n in seen:  # meglio iterare in seen così da eliminare duplicati
            if n-1 not in seen:
                length=1    # più efficiente partire da 1 dato che n sai gia che è in seen
                while (n+length) in seen:
                    length+=1
                longest=max(longest,length)
        return longest