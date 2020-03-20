import heapq
class Solution:
    def getLeastNumbers(self, arr, k):
         a = heapq.nsmallest(k, arr)
         return a
    def method_2(self, arr, k):
        if k == 0:
            return []
        arr_1 = [-x for x in arr[:k]]
        heapq.heapify(arr_1)
        for i in arr[k:]:
            if -arr_1[0] > i:
                heapq.heappop(arr_1)
                heapq.heappush(arr_1, -i)
        return [-x for x in arr_1]


if __name__ == "__main__":
    a = Solution()
    print(a.getLeastNumbers([0,1,2,1],1))
# 最小的k个数
# 可以用快排
# 最好的方式还是堆排（大数据的情况下）
# python 中默认的heapq是小顶堆,所以要去负后选出最大的k个数（即原数组中最小的k个数）
