class Solution:
    def maxProfit(self, prices) -> int:
        max_deal = 2
        days = len(prices)
        states = 2
        #dp = [[[0 for i in range(2)] for i in range(3)] for i in range(days)]
        dp = []
        for i in range(days):
            dp.append([[0,0],[0,0],[0,0]])
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        for i in range(1,days):
            for j in range(1,3):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                #print("dp[{}][{}][0] = max(dp[{}][{}][0], dp[{}][{}][1] + {})".format(i,j,i-1,j,i-1,j,prices[i]), dp[i][j][0])
                #print(" dp[{}][{}][1] = max(dp[{}][{}][0], dp[{}][{}][0] - {})".format(i,j,i-1,j,i-1,j-1,prices[i]),dp[i][j][1])
        #print(dp)
        return dp[days - 1][2][0]

class Solution_1:
    def maxProfit(self, prices) -> int:
        if len(prices) == 0:
            return 0
        first_buy = -1000000
        fisrt_sell = 0
        second_buy = -1000000
        second_sell = 0
        for i in prices:
            first_buy = max(first_buy, -i)
            fisrt_sell = max(fisrt_sell, first_buy + i)
            second_buy = max(second_buy, fisrt_sell - i)
            second_sell = max(second_sell,second_buy + i)
        return second_sell

a = Solution()
prices = [3,3,5,0,0,3,1,4]
print(a.maxProfit(prices))