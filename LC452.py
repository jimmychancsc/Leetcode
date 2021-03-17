class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        count = 1

        n = len(points)
        first_end = points[0][1]
        for i in range(1, n):
            if first_end < points[i][0]:
                count += 1
                first_end = points[i][1]
        return count