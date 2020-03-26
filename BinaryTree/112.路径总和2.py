# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum: int):
        ret = []
        if not root:
            return ret
        stack = [(root, root.val, [root.val])]
        while stack:
            node, path, trace = stack.pop()
            if path == sum and not node.left and not node.right:
                ret.append(trace)
            else:
                if node.left is not None:
                    trace_new = [x for x in trace]
                    trace_new.append(node.left.val)
                    stack.append((node.left, node.left.val + path, trace_new))
                if node.right is not None:
                    trace_new = [x for x in trace]
                    trace_new.append(node.right.val)
                    stack.append((node.right, node.right.val + path, trace_new))
            #print(len(stack))
        return ret