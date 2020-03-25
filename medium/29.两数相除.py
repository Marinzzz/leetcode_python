class Solution:
    def guanfang(self):
        def guanfag(dividend, divisor):  # 转化成二进制的除法
            sign = (dividend > 0) ^ (divisor > 0)
            dividend = abs(dividend)
            divisor = abs(divisor)
            count = 0
            # 把除数不断左移，直到它大于被除数
            while dividend >= divisor:
                count += 1
                divisor <<= 1
            result = 0
            while count > 0:
                count -= 1
                divisor >>= 1
                if divisor <= dividend:
                    result += 1 << count  # 这里的移位运算是把二进制（第count+1位上的1）转换为十进制
                    dividend -= divisor
            if sign: result = -result
            return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1

    def divide(self, dividend: int, divisor: int) -> int:

        def simple_divide(x ,y):
            count = 0
            while x >= y:
                x -= y
                count += 1
            return count, x

        sign = 1
        if dividend == 0:
            return 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            sign = -1
        if sign == 1 and dividend == -2147483648 and divisor == -1:
            return 2147483647
        if abs(dividend) < abs(divisor):
            return 0
        temp_dividend = str(abs(dividend))
        pos = 0
        ret = ""
        temp = 0
        first = -1
        while pos < len(temp_dividend):
            flag = 0
            while temp < abs(divisor) and pos < len(temp_dividend):
                temp = temp * 10 + int(temp_dividend[pos])
                pos += 1
                flag += 1
            if first == -1:
                first = pos
            ret += "0" * (flag - 1)
            if temp >= abs(divisor):
                shang, yushu = simple_divide(temp, abs(divisor))
                ret += str(shang)
                temp = yushu
        while ret and ret[0] == '0':
            ret = ret[1:]
        ret += "0" * ((len(temp_dividend) - first + 1) - len(ret))
        if sign > 0:
            return int(ret)
        else:
            return 0 - int(ret)

if __name__ == "__main__":
    a = Solution()
    print(a.divide(1060849722, 99958928))

"""
-1060849722
99958928

"""