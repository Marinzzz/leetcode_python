class Solution:
    def cal_n(self, n):
        ret = 0
        for i in range(1, n + 1):
            ret += i
        return ret

    def is_Valid(self, x, cal, target):
        for i in range(1, 100000):
            if x * i - cal == target:
                return [i, cal]
            if x * i - cal < target:
                pass
            if x * i - cal > target:
                return [-1, -1]

    def findContinuousSequence(self, target: int):
        ret = []
        for i in range(448, 1, -1):
            if target < self.cal_n(i):
                continue
            temp = self.is_Valid(i, self.cal_n(i - 1), target)
            if len(temp) != 2:
                print(i)
            if temp[0] != -1:
                ret.append([j for j in range(temp[0] - i + 1, temp[0] + 1)])
        return ret

a = Solution()
ret = a.findContinuousSequence(50252)
print(ret)
count = 0
for i in range(100000):
    count += i
    if count > 100000:
        print(i)
        break
