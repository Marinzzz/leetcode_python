class Solution:
    def partition(self, s: str):

        def isvalid(temp_s):
            temp_r = temp_s[::-1]
            if temp_r == temp_s:
                return True
            else:
                return False

        ret = []
        if isvalid(s):
            ret.append([s])
        stack = [[s]]
        while stack:
            now = []
            while stack:
                temp = stack.pop()
                not_huiwen = temp.pop()
                for i in range(1, len(not_huiwen)):
                    i_front = not_huiwen[:i]
                    i_back = not_huiwen[i:]
                    if isvalid(i_front) and isvalid(i_back):
                        temp.append(i_front)
                        temp.append(i_back)
                        ret.append([x for x in temp])
                        now.append([x for x in temp])
                        temp.pop()
                        temp.pop()
                    elif isvalid(i_front):
                        temp.append(i_front)
                        temp.append(i_back)
                        now.append([x for x in temp])
                        temp.pop()
                        temp.pop()
            stack = now
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.partition("cdd"))





