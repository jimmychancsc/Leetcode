class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        res[0] = 1
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        r = 1
        for i in range(n - 1, -1, -1):
            res[i] = r * res[i]
            r *= nums[i]

        return res