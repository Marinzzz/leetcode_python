import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = collections.Counter(s)
        count = 0
        for key,values in dic.items():
            count += values // 2
        ret = count * 2
        if ret < len(s):
            ret = ret + 1
        return ret