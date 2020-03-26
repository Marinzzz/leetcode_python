import BinaryTree.TreeNode
class Solution:
    def hasPathSum(self, root, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, path = stack.pop()
            if path == sum and not node.left and not node.right:
                return True
            else:
                if node.left is not None:
                    stack.append((node.left, node.left.val + path))
                if node.right is not None:
                    stack.append((node.right, node.right.val + path))
            #print(len(stack))
        return False