# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(left, right):
            nonlocal index
            if left > right:
                return None
            root_val = postorder[index]
            root = TreeNode(root_val)
            index -= 1
            root.right = helper(inorder_map[root_val] + 1, right)
            root.left = helper(left, inorder_map[root_val] - 1)
            return root

        index = len(postorder) - 1
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        return helper(0, len(inorder) - 1)