# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)

        def helper(root):
            if not root:
                return None
            if root in nodes:
                return root

            left, right = helper(root.left), helper(root.right)
            if left and right:
                return root
            if left:
                return left
            if right:
                return right

        return helper(root)