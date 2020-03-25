class SolutionMy:

    def minCut(self, s: str) -> int:
        def isvalid(temp_s):
            temp = temp_s[::-1]
            if temp == temp_s:
                return True
            else:
                return False

        stack = [s]
        count = 0
        while stack:
            new = []
            for now in stack:
                temp = now
                if len(temp) <= 1:
                    return count
                if isvalid(temp):
                    return count
                for i in range(1, len(temp)):
                    i_front = temp[:i]
                    i_back = temp[i:]
                    if isvalid(i_front) and isvalid(i_back):
                        return count + 1
                    elif isvalid(i_front):
                        new.append(i_back)
                    elif isvalid(i_back):
                        new.append(i_front)
                    else:
                        continue
            count += 1
            stack = new
        return count


class Solution:
    def minCut(self, s: str) -> int:
        if len(s) < 1:
            return 0
        r = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j + 1]
                if temp == temp[::-1]:
                    r[i][j] = True

        dp = [x for x in range(len(s))]
        dp[0] = 0
        for i in range(1, len(s)):
            if r[0][i]:
                dp[i] = 0
            else:
                for j in range(0, i):
                    if r[j + 1][i]:
                        dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]


if __name__ == "__main__":
    a = Solution()
    print(a.minCut("aab"))
