# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:

        def dfs(node):
            if not node or node.val == p or node.val == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right

        def dist(node, target):
            if not node:
                return float(inf)
            if node.val == target:
                return 0
            return 1 + min(dist(node.left, target), dist(node.right, target))

        LCA = dfs(root)
        return dist(LCA, p) + dist(LCA, q)