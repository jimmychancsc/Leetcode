class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (-x[0], x[1]))
        n = len(intervals)
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if intervals[i][1] <= intervals[j][1]:
                    count += 1
                    break
        return n - count
