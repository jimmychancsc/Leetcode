class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]
        for i in intervals:
            if i[0] > res[-1][1]:
                res.append(i)

            elif i[1] > res[-1][1]:
                res[-1][1] = i[1]

        return res
