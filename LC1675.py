class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        evens = []
        minimum = inf
        for num in nums:
            if num%2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num*2)
                minimum = min(minimum, num*2)
        heapq.heapify(evens)
        res = inf
        while evens:
            curr = -heapq.heappop(evens)
            res = min(res, curr-minimum)
            if curr %2 ==0:
                minimum = min(minimum, curr//2)
                heapq.heappush(evens,-curr//2)
            else:
                break
        return res