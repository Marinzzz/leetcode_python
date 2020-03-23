class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0
        row = len(dungeon)
        col = len(dungeon[0])
        dp = [[0 for i in range(col + 1)] for j in range(row + 1)]
        dp[row - 1][col - 1] = max(1, 1 - dungeon[row - 1][col - 1]) 
        for i in range(row - 2, -1, -1):
            dp[i][col - 1] = max(1, dp[i + 1][col - 1] - dungeon[i][col - 1]) 
        for j in range(col - 2, -1, -1):
            dp[row - 1][j] = max(1, dp[row - 1][j + 1] - dungeon[row - 1][j])
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]))
        #print(dp)
        return dp[0][0]