# 组合总和
# 用1-9中不同的数 K个 来构成n
# 思路一，模拟排列组合，选出所有可能的k个数一组的排列

class Solution:
    def combinationSum3(self, k, n):
        ret = []

        def getcombination(k, temp_arr, n):
            if len(temp_arr) == k and sum(temp_arr) == n:
                ret.append([i for i in temp_arr])
                return
            else:
                if temp_arr:
                    start = temp_arr[-1]
                else:
                    start = 1
                for i in range(start, 10):
                    if i not in temp_arr:
                        next = [x for x in temp_arr]
                        next.append(i)
                        getcombination(k, next)
                    else:
                        continue
        getcombination(k, [], n)
        return ret


