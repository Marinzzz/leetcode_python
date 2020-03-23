from collections import Counter
class Solution:
    def countCharacters(self, words, chars):
        my_chars = Counter(chars)
        count = 0
        for word in words:
            temp_chars = Counter(word)
            flag = 0
            for key,value in temp_chars.items():
                if key in my_chars and temp_chars[key] <= my_chars[key]:
                    continue
                else:
                    flag = 1
                    break
            if flag:
                count += len(word)
            else:
                continue
        return count

a = Solution()
print(a.countCharacters(["cat","bt","hat","tree"], "atach"))