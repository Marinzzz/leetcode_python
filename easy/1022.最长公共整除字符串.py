import math
def get_it(str1):
    ret = []
    length = len(str1)
    for i in range(length, 0, -1):
        if length % i == 0:
            temp_str = str1[0: i]
            if temp_str * int(length / i) == str1:
                ret.append(temp_str)
    return ret

str1 = "ABCABC"
str2 = "ABC"

ret1 = get_it(str1)
ret2 = get_it(str2)

for i in ret1:
    if i in ret2:
        print(i)
print("")

