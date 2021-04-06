# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: TreeNode):
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(node: TreeNode) -> List[int]:
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        def swap(nums: List[int]) -> (int, int):
            x, y = -1, -1

            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y

        def recover(r: TreeNode, count: int):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return
                recover(r.left, count)
                recover(r.right, count)

        nums = inorder(root)
        x, y = swap(nums)
        recover(root, 2)