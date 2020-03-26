class Solution:
    def candy(self, ratings) -> int:
        length = len(ratings)
        dp = [1] * length
        if length == 1:
            return 1
        dp[0] = 2 if ratings[0] > ratings[1] else 1
        ratings.append(100000000)
        for i in range(1, length):
            if ratings[i - 1] < ratings[i]:
                dp[i] = dp[i - 1] + 1
        for i in range(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i + 1] + 1)
        return sum(dp)


if __name__ == "__main__":
    a = Solution()
    print(a.candy([1,2,87,87,87,2,1]))