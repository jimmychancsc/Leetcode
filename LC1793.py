class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = mini = nums[k]
        i, j, n = k, k, len(nums)

        while i > 0 or j < n - 1:
            if (nums[i - 1] if i else 0) > (nums[j + 1] if j < n - 1 else 0):
                i -= 1
            else:
                j += 1

            mini = min(nums[i], nums[j], mini)
            res = max(res, mini * (j - i + 1))

        return res