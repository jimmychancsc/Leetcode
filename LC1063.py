class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        nextsmaller = [len(nums)] * len(nums)
        for i, v in enumerate(nums):
            while stack and stack[-1][1] > v:
                nextsmaller[stack.pop()[0]] = i
            stack.append([i, v])
        return sum(v-i for i, v in enumerate(nextsmaller))