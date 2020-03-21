class Solution:

    def countDigitOne(self, n: int) -> int:
        import math

        def countDigitOne(self, n: int) -> int:
            import math
            if n <= 0:
                return 0

            def recursion(temp_n):
                ret = 0
                if temp_n == 0:
                    return 0
                if temp_n < 10:
                    return 1
                str_n = str(temp_n)
                length = len(str_n)
                ret += (length - 1) * pow(10, length - 2)
                if str_n[0] < '2':
                    ret += temp_n - int('9' * (length - 1))
                    ret += recursion(int(str_n[1:]))
                else:
                    ret += math.pow(10, length - 1)
                    ret += (int(str_n[0]) - 1) * (length - 1) * pow(10, length - 2)
                    ret += recursion(int(str_n[1:]))
                return ret
            return int(recursion(n))


if __name__ == "__main__":
    a = Solution()
    print(a.countDigitOne(12345))
#0~9 1
#0~99 20
#0~999 300
#10000 4000
