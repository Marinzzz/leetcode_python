import BinaryTree.TreeNode
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            new = []
            temp = []
            for node in stack:
                temp.append(node.val)
                if node.left:
                    new.append(node.left)
                if node.right:
                    new.append(node.right)
            ret.append(temp)
            stack = new
        return ret