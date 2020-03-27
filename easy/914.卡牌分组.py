import collections
class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        d = collections.Counter(deck)
        l = sorted(d.items(), key=lambda item:item[1])
        #return True if d[-1][1] >= 2 else
        if l[0][1] == 1:
            return False
        for i in range(2, l[0][1] + 1):
            flag = 0
            for j in l:
                if j[1] % i != 0:
                    flag = 1
                    break
                else:
                    continue
            if flag == 0:
                return True
        return False

"""
学到一个gcd函数
    public int gcd(int x, int y) {
        return x == 0 ? y : gcd(y%x, x);
    }

"""