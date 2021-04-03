class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        l, r = 1, sum(sweetness) // (K + 1)
        while l < r:
            m = (l + r + 1) // 2

            curr = 0
            cuts = 0
            for s in sweetness:
                curr += s
                if curr >= m:
                    cuts += 1
                    curr = 0
            if cuts > K:
                l = m
            else:
                r = m - 1
        return r
