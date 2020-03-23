# 题型dp
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

    def rob_1(self, nums):  # 没有dp数组的情况
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        prev = nums[0]
        now = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = max(prev + nums[i], now)
            prev = now
            now = temp
        return now