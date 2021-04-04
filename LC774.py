class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(D):
            return sum(int((stations[i + 1] - stations[i]) / D) for i in range(len(stations) - 1)) <= k

        l, r = 0, stations[-1] - stations[0]

        while r - l > 1e-6:
            m = (r + l) / 2
            if possible(m):
                r = m
            else:
                l = m
        return l

