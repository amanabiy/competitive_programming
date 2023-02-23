class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        check = [False, False]

        if min(x2, rec2[2]) > max(x1, rec2[0]):
            check[0] = True
        if min(y2, rec2[3]) > max(y1, rec2[1]):
            check[1] = True
        
        return check[0] and check[1]