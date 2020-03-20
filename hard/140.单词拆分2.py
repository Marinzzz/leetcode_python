class Solution:
    ret = []
    hashmap = {}

    def wordBreak(self, s: str, wordDict):
        def recursion(str1, dic, sentence):
            if str1 == "":
                import copy
                self.ret.append(copy.deepcopy(sentence))
            for i in range(1, len(str1) + 1):
                if str1[:i] in dic:
                    sentence.append(str1[:i])
                    recursion(str1[i:], dic, sentence)
                    sentence.pop()
                else:
                    continue
            return

        # 递归解法
        # b = []
        # recursion(s, wordDict, b)
        # return self.ret

        # 记忆化的搜索
        def search_memory(str1, dic, start):
            res = []
            if start in self.hashmap:
                return self.hashmap[start]
            else:
                if start == len(str1):
                    res.append("")
                    print(res)
                for i in range(start + 1, len(str1) + 1):
                    if str1[start: i] in dic:
                        nextret = search_memory(str1, dic, i)
                        for word in nextret:
                            mid = "" if word == "" else " "
                            # print(str1[start: i] + mid + word)
                            res.append(str1[start: i] + mid + word)
                            # print(res)
            self.hashmap[start] = res
            return res

        return search_memory(s, wordDict, 0)


if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    a = Solution()
    print(a.wordBreak(s, wordDict))
