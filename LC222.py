# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depth(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exist(self, idx: int, d: int, node: TreeNode) -> bool:
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            mid = left + (right - left) // 2
            if idx <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = self.depth(root)
        if d == 0:
            return 1

        left, right = 1, 2 ** d - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.exist(mid, d, root):
                left = mid + 1
            else:
                right = mid - 1

        return (2 ** d - 1) + left