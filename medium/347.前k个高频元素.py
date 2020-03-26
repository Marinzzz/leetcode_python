"""
思路1.Counter，即统计后输出


"""


class Solution:
    def topKFrequent(self, nums, k):
        ret = []
        from collections import Counter
        r = Counter(nums)
        q = sorted(r.items(), key=lambda item : item[1], reverse=True)
        for i in range(k):
            ret.append(q[i][0])
        return ret






if __name__ == "__main__":
    a = Solution()
    ret = a.topKFrequent([1,213,3,2,1,2,3,2,3,3,2,3,3,3,3,3,3,3,3,452,25,52,5,254,25,25,25,25,25,25], 3)
    print(ret)