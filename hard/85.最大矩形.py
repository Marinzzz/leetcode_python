class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        ret = 0
        def get_array_matrix(dp):
            max_area = 0
            stack = [0]
            for i in range(len(dp)):
                while stack and stack[-1] > dp[i]:
                    temp = stack.pop()
                    max_area = max(max_area, dp[temp] * (i - 1 - stack[-1] - 1 + 1))
                stack.append(i)
            while stack and stack[-1] > 0:
                temp = stack.pop()
                max_area = max(max_area, dp[temp] * (len(dp) - 1 - stack[-1] - 1 +1))
            return max_area
        dp = 0 * (len(matrix[0]))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == 1 else 0
            ret = max(ret, get_array_matrix(dp))
