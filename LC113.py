# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, remainingSum, path, res):
        if not node:
            return
        path.append(node.val)
        if remainingSum == node.val and not node.left and not node.right:
            res.append(list(path))
        else:
            self.dfs(node.left, remainingSum - node.val, path, res)
            self.dfs(node.right, remainingSum - node.val, path, res)

        path.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res