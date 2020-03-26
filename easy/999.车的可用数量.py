class Solution:
    def numRookCaptures(self, board) -> int:
        count = 0
        rook_i = 0
        rook_j = 0
        raw = len(board)
        col = len(board[0])
        for i in range(raw):
            for j in range(col):
                if board[i][j] == 'R':
                    rook_i = i
                    rook_j = j
                    break
        # 向上
        for i in range(rook_i - 1, -1, -1):
            if board[i][rook_j] == 'p':
                count += 1
                break
            if board[i][rook_j] == 'B':
                break
            else:
                continue
        # 向下
        for i in range(rook_i + 1, raw):
            if board[i][rook_j] == 'p':
                count += 1
                break
            if board[i][rook_j] == 'B':
                break
            else:
                continue
        # 向左
        for j in range(rook_j - 1, -1, -1):
            if board[rook_i][j] == 'p':
                count += 1
                break
            if board[rook_i][j] == 'B':
                break
            else:
                continue
        # 向右
        for j in range(rook_j + 1, col):
            if board[rook_i][j] == 'p':
                count += 1
                break
            if board[rook_i][j] == 'B':
                break
            else:
                continue
        return count