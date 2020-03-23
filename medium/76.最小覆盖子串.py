from collections import Counter
def main():
    s = "a"
    t = "a"
    dict_t = Counter(t)
    required = len(dict_t)
    temp_feed = 0 #已经满足的字符
    l = 0
    r = 0 #左右指针
    temp_window_dict = {} #目前滑动窗口内的字符字典
    ret = (1000000,1,1)
    while r < len(s):
        temp_window_dict[s[r]] = temp_window_dict.get(s[r], 0) + 1
        if s[r] in dict_t and temp_window_dict[s[r]] == dict_t[s[r]]:
            temp_feed += 1
        while l < r and temp_feed == required:
            if r - l + 1 < ret[0]:
                ret = (r - l + 1, l, r)
            temp_window_dict[s[l]] -= 1
            if s[l] in dict_t and temp_window_dict[s[l]] < dict_t[s[l]]:
                temp_feed -= 1
            l += 1
        r += 1
    return "" if ret[0] == 1000000 else s[ret[1] : ret[2] + 1]
ret = main()
print(ret)