class Solution:
    def isRectangleOverlap(self, rec1, rec2) -> bool:
        count = 0
        if rec1[0] >= rec2[2]:
            count += 1
        if rec1[2] <= rec2[0]:
            count += 1
        if rec1[1] >= rec2[3]:
            count += 1
        if rec1[3] <= rec2[1]:
            count += 1
        if count >= 1:
            return False
        else:
            return True