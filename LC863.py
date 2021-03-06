# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def dfs(node, par):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        queue = collections.deque([(target, 0)])
        seen = set([target])
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    queue.append((nei, d + 1))
                    seen.add(nei)

        return []