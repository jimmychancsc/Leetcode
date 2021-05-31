class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        maxi = -1
        left = 0
        current = 0

        for right in range(n):
            current += nums[right]
            while current > total-x and left <= right:
                current -= nums[left]
                left += 1
            if current == total-x:
                maxi = max(maxi, right-left+1)

        return n-maxi if maxi != -1 else -1