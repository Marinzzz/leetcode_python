class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s and not p:
            return True
        if not s and len(p) == 1:
            return False
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(2, len(p) + 1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i - 2]
        #如果没有这个初始化会怎么样？会过不了s="" p="a*"这种
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == "." or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] != s[i - 1] and p[j - 2] != '.':
                        dp[i][j] = dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                else:
                    dp[i][j] = False
        return dp[len(s)][len(p)]

a = Solution()
print(a.isMatch("","a*b*"))