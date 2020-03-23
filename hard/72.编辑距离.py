word1 = "abcde"
word2 = "abc"
ret = 0
cur1 = 0
cur2 = 0
while(len(word1) < len(word2)):
     #需要增加元素
    while(word1[cur1] == word2[cur2]):
        cur1 += 1
        cur2 += 1
        if cur1 == len(word1):
            cur1 -= 1
    word1 = word1[0:cur1] + word2[cur2] + word1[cur1:]
    ret += 1
while(len(word1) > len(word2)):
    #需要删除元素
    while(word1[cur1] == word2[cur2]):
        cur1 += 1
        cur2 += 1
        if cur2 == len(word2):
            cur2 -= 1
    word1 = word1[0:cur1] + word1[cur1 + 1:]
    ret += 1
## 进行替换
for i in range(len(word1)):
    if word1[i] == word2[i]:
        continue
    else:
        word1[i] == word2[i]
        ret += 1
print(ret)
