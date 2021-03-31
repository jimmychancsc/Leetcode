class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        l, r = 1, max(bloomDay)

        while l < r:
            mid = (l + r) // 2
            flow = bout = 0
            for b in bloomDay:
                flow = 0 if b > mid else flow + 1
                if flow >= k:
                    flow = 0
                    bout += 1
                    if bout == m:
                        break
            if bout == m:
                r = mid
            else:
                l = mid + 1

        return l