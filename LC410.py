class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = 0, 0
        n = len(nums)
        for i in range(n):
            r += nums[i]
            if l < nums[i]:
                l = nums[i]

        res = r
        while l <= r:
            mid = (l + r) // 2
            summ = 0
            count = 1
            for i in range(n):
                if summ + nums[i] > mid:
                    count += 1
                    summ = nums[i]
                else:
                    summ += nums[i]
            if count <= m:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res