class Solution:
    def shortestPalindrome(self, s: str) -> str:

        def is_valid(temps):
            if temps == temps[::-1]:
                return True
            else:
                return False

        if len(s) == 1 or is_valid(s):
            return 0
        prev = 0
        back = len(s) - 1
        while prev <= back:
            if s[prev] == s[back]:
                prev += 1
                back -= 1
            else:
                break
        add_str = ""
        if prev == 0:
        for i in range(1, prev):
            if not is_valid(s[0, i + 1]):
                add_str = s[i :]
                add_str = add_str[::-1]

        return add_str + s


if __name__ == "__main__":
    a = Solution()
    print(a.shortestPalindrome("aafihaifalfafaskfjalkfjalkbcd"))