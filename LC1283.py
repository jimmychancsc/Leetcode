class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l < r:
            mid = (l + r) // 2
            if sum((i + mid - 1) // mid for i in nums) > threshold:
                l = mid + 1
            else:
                r = mid

        return l