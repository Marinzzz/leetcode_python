import functools


class Solution:
    flag = 0

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def dp_str(str1, str2, str3):
            if len(s1) + len(s2) != len(s3):
                return False
            if len(s1) == 0 and len(s2) == 0:
                return True
            dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
            dp[0][0] = True
            for i in range(1, len(s1) + 1):
                dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
            for j in range(1, len(s2) + 1):
                dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
            for i in range(1, len(s1) + 1):
                for j in range(1, len(s2) + 1):
                    dp[i][j] = (dp[i - 1][j] and True if s1[i - 1] == s3[i + j - 1] else False) or (
                        dp[i][j - 1] and True if s2[j - 1] == s3[i + j - 1] else False)
            return dp[len(s1)][len(s2)]
        return dp_str(s1, s2, s3)
        # 递归写法
        self.flag = 0

        @functools.lru_cache(None)
        def recursion_str(str1, str2, str3):
            if self.flag == 1:
                return
            if str3 == "" and str1 == "" and str2 == "":
                self.flag = 1
            for i in range(1, len(str1) + 1):
                if str1[:i] == str3[:i]:
                    recursion_str(str1[i:], str2, str3[i:])
                else:
                    break
            for i in range(1, len(str2) + 1):
                if str2[:i] == str3[:i]:
                    recursion_str(str2[i:], str1, str3[i:])
                else:
                    break
            return

        recursion_str(s1, s2, s3)
        if self.flag == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    a = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(a.isInterleave(s1, s2, s3))

# 题型： 使用递归和dp都可以,递归会超时，可以使用functools装饰器
# 字符
# "aabc"
# "abad"
# "aabacbad"

# dp 思路
