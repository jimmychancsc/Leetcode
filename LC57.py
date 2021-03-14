class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        left, right = newInterval
        i, n = 0, len(intervals)

        while i < n and left > intervals[i][0]:
            res.append(intervals[i])
            i += 1

        if not res or res[-1][1] < left:
            res.append(newInterval)

        else:
            res[-1][1] = max(res[-1][1], right)

        while i < n:
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
                i += 1
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
                i += 1

        return res