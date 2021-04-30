class Solution:

    def pathSum(self, nums: List[int]) -> int:
        self.ans = 0
        values = {x // 10: x % 10 for x in nums}

        def dfs(node, curr_sum):
            if node not in values:
                return
            curr_sum += values[node]
            depth, pos = divmod(node, 10)
            left = (depth + 1) * 10 + pos * 2 - 1
            right = left + 1

            if left not in values and right not in values:
                self.ans += curr_sum

            else:
                dfs(left, curr_sum)
                dfs(right, curr_sum)

        dfs(nums[0] // 10, 0)

        return self.ans
