def numDecodings(s):
    if s[0] == '' or not s:
        return 0
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(1, len(s)):
        if s[i] == '0':
            if(s[i - 1] == '1' or s[i - 1] == '2'):
                dp[i + 1] = dp[i - 1]
            else:
                return 0
        else:
            if s[i - 1] == '1' or (s[i - 1] == '2' and "1" <= s[i] <= '6'):
                dp[i + 1] = dp[i] + dp[i - 1]
            else:
                dp[i + 1] = dp[i]
    print(dp)
def test(s):
    if s[0] == '' or not s:
        return 0
    dp_0 = 1
    dp_1 = 1
    for i in range(1, len(s)):
        if s[i] == '0':
            if(s[i - 1] == '1' or s[i - 1] == '2'):
                temp = dp_0
                dp_0 = dp_1
                dp_1 = temp
            else:
                return 0
        else:
            if s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6'):
                temp = dp_1
                dp_1 = dp_1 + dp_0
                dp_0 = temp
            else:
                dp_0 = dp_1
    print(dp_1)

s = '226'
numDecodings(s)
test(s)



