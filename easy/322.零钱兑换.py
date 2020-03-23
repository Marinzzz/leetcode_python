class Solution:
    record = 100000000
    def count_it(self, coins, amount, temp_amount, count):
        if temp_amount > amount:
            return
        for coin in coins:
            if temp_amount + coin == amount:
                self.record = count + 1 if (count + 1) < self.record else self.record
            if temp_amount + coin > amount:
                continue
            if temp_amount + coin < amount:
                self.count_it(coins,amount,temp_amount + coin, count + 1)

    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        for coin in coins:
            dp[coin] = 1
        for i in range(amount):
            if dp[i] != amount + 1:
                for coin in coins:
                    if i + coin > amount:
                        continue
                    dp[i + coin] = min(dp[i] + 1, dp[i + coin])
        if dp[amount] == amount + 1:
            return -1
        else:
            return dp[amount]
        #self.count_it(coins, amount, 0, 0)
        #print(self.record)

a = Solution()
coins = [1,2,5]
amount = 100
ret = a.coinChange(coins, amount)
print(ret)