class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        ASum = sum(nums)
        nums.sort(reverse=True)
        if ASum % k != 0:
            return False
        target = [ASum / k] * k

        def dfs(pos):
            if pos == len(nums): return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += nums[pos]
            return False
        return dfs(0)