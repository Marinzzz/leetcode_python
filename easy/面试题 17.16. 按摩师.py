class Solution:
    def massage(self, nums) -> int:
        if not nums:
            return 0
        prev = 0
        now = 0
        for i in nums:
            temp = max(now, prev + i)
            prev = now
            now = temp
        return now