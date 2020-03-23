class Solution:
    def isValid(self, i, j, max_i, max_j,grid,vis):
        if i >= 0 and i <= max_i and j >= 0 and j <= max_j:
            if grid[i][j] == 1 and vis[i][j] == 0:
                return True
            return False
        else:
            return False

    def orangesRotting(self, grid):
        max_i = len(grid) - 1
        max_j = len(grid[0]) - 1
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        bad_count = 0
        orange_all = 0
        if max_i < 0 or max_j < 0:
            return 0
        time = 0
        bad = []
        vis = [[0 for i in range(10)]for i in range(10)]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    bad_one = [i, j]
                    bad.append(bad_one)
                    bad_count += 1
                if grid[i][j] != 0:
                    orange_all += 1
        print(bad)
        while (True):
            new_bad = []
            for bad_one in bad:
                for i in range(0, 4):
                    new_x = bad_one[0] + dx[i]
                    new_y = bad_one[1] + dy[i]
                    if self.isValid(new_x, new_y, max_i, max_j, grid, vis):
                        vis[new_x][new_y] = 1
                        new_bad.append([new_x, new_y])
                        bad_count += 1
            if len(new_bad) == 0:
                break
            else:
                bad = new_bad
                time += 1
            print(bad)
        if bad_count == orange_all:
            return time
        else:
            return -1
a = Solution()
test = [[2,1,1],[1,1,0],[0,1,1]]
print(a.orangesRotting(test))
