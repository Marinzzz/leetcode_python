from BinaryTree import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1

        def get_depth(node):
            if not node:
                return 0
            L = get_depth(node.left)
            R = get_depth(node.right)
            self.ans = max(self.ans, L + R + 1)
            return max(L, R) + 1

        get_depth(root)
        return self.ans - 1
