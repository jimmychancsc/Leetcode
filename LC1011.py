class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid, curr, need = (l + r) // 2, 0, 1
            for w in weights:
                if w + curr > mid:
                    need += 1
                    curr = 0
                curr += w
            if need > D:
                l = mid + 1
            else:
                r = mid
        return l