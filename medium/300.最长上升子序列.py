class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ret = 0
        d = []
        for i in range(len(nums)):
            if not d or nums[i] > d[-1]:
                d.append(nums[i])
            else:
                l, r = 0, len(d) - 1
                pos = r
                while(l <= r):
                    mid = int(l + r / 2)
                    if d[mid] >= nums[i]:
                        pos = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[pos] = nums[i]

        return len(d)






'''
[10,9,2,5,3,7,101,18]
dp[i] 以第i个元素为结尾的最长上升子序列长度
dp[i] = max(dp[j]) + 1, for j in range(j - 1) if nums[i] > nums[j]

'''
