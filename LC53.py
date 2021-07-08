class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        lcmax = glbmax = nums[0]

        for i in range(1, len(nums)):
            lcmax = max(lcmax + nums[i], nums[i])
            glbmax = max(glbmax, lcmax)

        return glbmax