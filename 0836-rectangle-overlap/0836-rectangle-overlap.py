class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        x1, y1, x2, y2 = rec1
        xx1, yy1, xx2, yy2 = rec2

        if x2 <= xx1 or y2 <= yy1 or xx2 <= x1 or yy2 <= y1:
            return False

        return True