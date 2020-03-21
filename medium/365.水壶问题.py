class Solution:
    flag = 0
    hashmap = []

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        self.flag = 0
        self.hashmap = []

        def loop_stack(m_1, m_2, m_3):
            record = set()
            stack = [(0, 0)]
            while stack:
                temp_x, temp_y = stack.pop()
                if temp_x == m_3 or temp_y == m_3 or temp_x + temp_y == m_3:
                    return True
                if (temp_x, temp_y) in record:
                    continue
                record.add((temp_x, temp_y))
                stack.append((0, temp_y))
                stack.append((temp_x, 0))
                stack.append((x, temp_y))
                stack.append((temp_x, y))
                stack.append((temp_x - min(temp_x, y - temp_y), temp_y + min(temp_x, y - temp_y)))
                stack.append((temp_x + min(temp_y, x - temp_x), temp_y - min(temp_y, y - temp_y)))
            return False

        def recursion(temp_x, temp_y, m_1, m_2, m_3):
            if self.flag:
                return
            else:
                if temp_x == m_3 or temp_y == m_3 or temp_x + temp_y == m_3:
                    self.flag = 1
                    return
                else:
                    if temp_x > 0:
                        if [0, temp_y] not in self.hashmap:
                            self.hashmap.append([0, temp_y])
                            recursion(0, temp_y, m_1, m_2, m_3)
                    if temp_y > 0:
                        if [temp_x, 0] not in self.hashmap:
                            self.hashmap.append([temp_x, 0])
                            recursion(temp_x, 0, m_1, m_2, m_3)
                    if temp_x < m_1:
                        if [m_1, temp_y] not in self.hashmap:
                            self.hashmap.append([m_1, temp_y])
                            recursion(m_1, temp_y, m_1, m_2, m_3)
                    if temp_y < m_2:
                        if [temp_x, m_2] not in self.hashmap:
                            self.hashmap.append([temp_x, m_2])
                            recursion(temp_x, m_2, m_1, m_2, m_3)
                    if temp_x < m_1 and temp_y > 0:
                        if temp_y > (m_1 - temp_x):
                            if [m_1, temp_y - m_1 + temp_x] not in self.hashmap:
                                self.hashmap.append([m_1, temp_y - m_1 + temp_x])
                                recursion(m_1, temp_y - m_1 + temp_x, m_1, m_2, m_3)
                        else:
                            if [temp_x + temp_y, 0] not in self.hashmap:
                                self.hashmap.append([0, temp_y])
                                recursion(temp_x + temp_y, 0, m_1, m_2, m_3)
                    if temp_x > 0 and temp_y < m_2:
                        if temp_x > (m_2 - temp_y):
                            if [temp_x - m_2 + temp_y, m_2] not in self.hashmap:
                                self.hashmap.append([0, temp_y])
                                recursion(temp_x - m_2 + temp_y, m_2, m_1, m_2, m_3)
                        else:
                            if [0, temp_x + temp_y] not in self.hashmap:
                                self.hashmap.append([0, temp_x + temp_y])
                                recursion(0, temp_x + temp_y, m_1, m_2, m_3)
                    return
        return loop_stack(x, y, z)
        self.hashmap.append([0, 0])
        recursion(0, 0, x, y, z)
        if self.flag == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    a = Solution()
    print(a.canMeasureWater(3, 4, 5))
