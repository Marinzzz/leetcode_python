class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f

if __name__ == "__main__":
    a = Solution()
    a.lastRemaining(5, 3)