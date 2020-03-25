class Solution:
    def surfaceArea(self, grid):

        def IsValid(tempx, tempy):
            if 0 <= tempx < row and 0 <= tempy < col and grid[x][y]:
                return True

        ret = 0
        row = len(grid)
        col = len(grid[0])
        dx =[1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        vis = [[0 for i in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                if not grid[i][j]:
                    continue
                temp = 0
                if grid[i][j]:
                    temp += 2 + 4 * grid[i][j]
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if IsValid(x, y):
                        temp -= min(grid[i][j], grid[x][y])
                ret += temp
        return ret


if __name__ == "__main__":
    a = Solution()
    print(a.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))




