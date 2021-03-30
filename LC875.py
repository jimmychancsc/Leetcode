class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible(K):
            return sum((p - 1) // K + 1 for p in piles) <= h

        lo, hi = 1, max(piles)
        while lo < hi:
            mid = (lo + hi) // 2
            if not possible(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo