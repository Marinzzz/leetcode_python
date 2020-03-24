class Solution:

    def Isvaliid(self, temp_s):
        stack = []
        if not temp_s:
            return True
        for i in temp_s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if stack:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False

    def removeInvalidParentheses(self, s: str):
        ret = set()
        stack = [s]
        flag = 0
        while stack:
            new = []
            for i in stack:
                if self.Isvaliid(i):
                    flag = 1
                    ret.add(i)
                else:
                    if flag:
                        continue
                    count_left = i.count('(')
                    count_right = i.count(')')
                    if count_left > count_right: # 需要删除左括号，随便删一个？
                        for j in range(len(i)):
                            if i[j] == '(':
                                temp = i[:j] + i[j + 1:]
                                if temp not in new:
                                    new.append(temp)
                    elif count_left < count_right:
                        for j in range(len(i)):
                            if i[j] == ')':
                                temp = i[:j] + i[j + 1:]
                                if temp not in new:
                                    new.append(temp)
                    else:
                        for j in range(len(i)):
                            if i[j] == '(' or i[j] == ')':
                                temp = i[:j] + i[j + 1:]
                                if temp not in new:
                                    new.append(temp)
            stack = new

        return ret


if __name__ == "__main__":
    a = Solution()
    s = "))(((((()())(()"
    print(a.removeInvalidParentheses(s))










