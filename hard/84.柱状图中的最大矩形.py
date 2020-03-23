class Solution:
    '''
        def largestRectangleArea(self, heights):
        max_area = 0
        record = [[-1 for i in range(len(heights))] for i in range(len(heights))]
        for i in range(len(heights)):
            record[i][i] = heights[i]
        for i in range(0,len(heights)):
            for j in range(i + 1,len(heights)):
                record[i][j] = min([record[i][j - 1], heights[j]])
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                temp = record[i][j] * (j - i + 1)
                if temp > max_area:
                    max_area = temp
                #print(record[i][j], end=' ')
            #print("")
        return max_area
    '''
    def largestRectangleArea2(self, heights) -> int:
        stack = [0]
        res = 0
        for i in range(1, len(heights)):
            while heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                print(tmp)
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res

    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # print(stack)
            flag = 1
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                if flag:
                    print("开始进行出栈操作")
                    print("栈顶元素和正在遍历的元素{},{}".format(tmp,i))
                    flag = 0
                res = max(res, (i - stack[-1] - 1) * heights[tmp])#这里的柱子是从第stack[-1] + 1 到 第i - 1根柱子
                print("第{0}根柱子出栈，长度为{1}".format(tmp, heights[tmp]))
                print("此时计算的长度为从{}到{}(不包括{}),最短柱子为第{}根柱子，长度为{}".format(stack[-1] + 1, i, i, tmp, heights[tmp]))
                print("目前栈内柱子高度情况：",end="")
                print([heights[pos] for pos in stack])
                print("目前栈内柱子下标情况:", end="")
                print(stack)
            stack.append(i)
            print("第{0}根柱子进栈，长度为{1}".format(i, heights[i]))
            print("目前栈内情况：", end="")
            print([heights[pos] for pos in stack])
            print("目前栈内柱子下标情况:", end="")
            print(stack)
        return res


a = Solution()
test = [5,4,3,2,1,2,3,4,5]
#print(a.largestRectangleArea(test))
print(a.largestRectangleArea2([2,1,5,6,2,3]))

