# 题型 DP
"""
相比198那道题，这道题的意思就是第一个房子和最后一个房子只能选一个偷，那么也就是说
可以划分成


"""


class Solution:

    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        record = [0] * len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        record[0] = 1
        dp[1] = max(nums[0], nums[1])
        if nums[0] > nums[1]:
            record[1] = 1
        for i in range(2, len(nums) - 1):
            if dp[i - 1] < dp[i - 2] + nums[i]:
                dp[i] = dp[i - 2] + nums[i]
                record[i] = record[i - 2]
            else:
                dp[i] = dp[i - 1]
                record[i] = record[i - 1]
        t = dp[len(nums) - 3] + nums[-1] if record[-3] == 0 else 0
        dp[-1] = max(t, dp[-2])
        return dp[-1]


if __name__ == "__main__":
    a = Solution()
    b = [1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]
    print(a.rob(b))