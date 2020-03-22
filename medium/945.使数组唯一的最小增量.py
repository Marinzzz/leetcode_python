"""

3 2 1 2 1 7
首先进行一个排序
1 1 2 2 3 7

"""


class Solution:
    def minIncrementForUnique(self, A) -> int:
        A.sort()
        count = 0
        for i in range(1, len(A)):
            count += max(0, A[i - 1] - A[i] + 1)
            A[i] += max(0, A[i - 1] - A[i] + 1)
        return count

    def no_sort(self, A):
        max_A = -1
        record = [0] * 40001
        ret = 0
        for i in A:
            record[i] += 1
            max_A = max(max_A, i)
        for i in range(max_A + 1):
            if record[i] > 1:
                temp = record[i] - 1
                ret += temp
                record[i + 1] += temp
                record[i] = 1
        temp = record[max_A + 1] - 1
        ret += temp * (temp + 1) / 2
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.no_sort([1, 2, 2]))
