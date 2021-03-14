class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []

        left, right = toBeRemoved

        for start, end in intervals:
            if start > right or end < left:
                res.append([start, end])
            else:
                if start < left:
                    res.append([start, left])
                if end > right:
                    res.append([right, end])

        return res