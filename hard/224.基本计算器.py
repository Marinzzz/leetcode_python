# 思路非常清晰
# 中缀转后缀
# 后缀表达式求值
# 今天对中缀表达式有了新的理解，中缀表达式实际上就是维护一个运算符等级递增的一个递增栈
# 为什么栈内的相同的符号的优先级要比栈外的高？ 因为运算的优先级是从左到右。
# 为什么遇见左括号可以直接入栈，因为我们总是先计算括号内的运算符
"""
1.从左到右进行遍历
2.运算数,直接输出.
3.左括号,直接压入堆栈,(括号是最高优先级,无需比较)(入栈后优先级降到最低,确保其他符号正常入栈)
4.右括号,(意味着括号已结束)不断弹出栈顶运算符并输出直到遇到左括号(弹出但不输出)
5.运算符,将该运算符与栈顶运算符进行比较,
如果优先级高于栈顶运算符则压入堆栈(该部分运算还不能进行),
如果优先级低于等于栈顶运算符则将栈顶运算符弹出并输出,然后比较新的栈顶运算符.
(低于弹出意味着前面部分可以运算,先输出的一定是高优先级运算符,等于弹出是因为同等优先级,从左到右运算)
直到优先级大于栈顶运算符或者栈空,再将该运算符入栈.
6.如果对象处理完毕,则按顺序弹出并输出栈中所有运算符.
"""

# 运行速度比较慢
class Solution:

    def calculate(self, s: str) -> int:
        def trans(original):
            stack = []
            ret = []
            temp = 0
            length = len(s)
            i = 0
            while i < length:
                # 如果i是数字
                if '0' <= s[i] <= '9':
                    temp = int(s[i])
                    if i < len(s) - 1 and '0' <= s[i + 1] <= '9':
                        while i < len(s) - 1 and '0' <= s[i + 1] <= '9':
                            temp = temp * 10 + int(s[i + 1])
                            i += 1
                    i += 1
                    ret.append(temp)
                    continue
                else:
                    if s[i] == '(':
                        stack.append(s[i])
                    elif s[i] == ')':
                        while stack:
                            c = stack.pop()
                            if c == '(':
                                break
                            else:
                                ret.append(c)
                    elif s[i] == '+' or s[i] == '-':
                        if stack and stack[-1] == '(':
                            stack.append(s[i])
                        else:
                            while stack and stack[-1] != '(':
                                c = stack.pop()
                                ret.append(c)
                            stack.append(s[i])
                    else:
                        pass
                    i += 1
            while stack:
                ret.append(stack.pop())
            print(ret)
            return ret

        def cal(trans_str):
            stack = []
            for i in trans_str:
                if i == '+':
                    a = stack.pop()  # 后面的操作数
                    b = stack.pop()  # 前面的操作数
                    stack.append(b + a)
                elif i == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                else:
                    stack.append(i)
            return stack[-1]
        trans_str = trans(s)
        return cal(trans_str)

# 官方题解
class answer_Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0 # For the on-going result
        sign = 1 # 1 means positive, -1 means negative

        for ch in s:
            if ch.isdigit():

                # Forming operand, since it could be more than one digit
                operand = (operand * 10) + int(ch)

            elif ch == '+':

                # Evaluate the expression to the left,
                # with result, sign, operand
                res += sign * operand

                # Save the recently encountered '+' sign
                sign = 1

                # Reset operand
                operand = 0

            elif ch == '-':

                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':

                # Push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)

                # Reset operand and result, as if new evaluation begins for the new sub-expression
                sign = 1
                res = 0

            elif ch == ')':

                # Evaluate the expression to the left
                # with result, sign and operand
                res += sign * operand

                # ')' marks end of expression within a set of parenthesis
                # Its result is multiplied with sign on top of stack
                # as stack.pop() is the sign before the parenthesis
                res *= stack.pop() # stack pop 1, sign

                # Then add to the next operand on the top.
                # as stack.pop() is the result calculated before this parenthesis
                # (operand on stack) + (sign on stack * (result from parenthesis))
                res += stack.pop() # stack pop 2, operand

                # Reset the operand
                operand = 0

        return res + sign * operand

if __name__ == "__main__":
    s = "(1+(4+5+2)-3)+(6+8)"
    a = answer_Solution()
    print(a.calculate(s))
