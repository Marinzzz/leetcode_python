from BinaryTree import TreeNode


class Solution_1:  # 递归
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ret = []
        if not root:
            return ret

        def recursion(Node, temp_str):
            if not Node.left and not Node.right:
                ret.append(temp_str)
            if Node.left:
                recursion(Node.left, temp_str + "->" + str(Node.left.val))
            if Node.right:
                recursion(Node.right, temp_str + "->" + str(Node.right.val))

        recursion(root, str(root.val))
        return ret
class Solution_2:    # 非递归
    def binaryTreePaths(self, root):
        ret = []
        if not root:
            return ret
        stack = [(root, str(root.val))]
        while(stack):
            tempNode, tempstr = stack.pop()
            if not tempNode.left and not tempNode.right:
                ret.append(tempstr)
            if tempNode.left:
                stack.append((tempNode.left, tempstr + "->" + str(tempNode.left.val)))
            if tempNode.right:
                stack.append((tempNode.right, tempstr + "->" + str(tempNode.right.val)))
        return ret
