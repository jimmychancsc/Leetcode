class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        if not slots1 or not slots2:
            return []

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])

        n1, n2 = len(slots1), len(slots2)
        i, j = 0, 0

        while i < n1 and j < n2:
            if slots1[i][1] <= slots2[j][0]:
                i += 1
            elif slots1[i][0] >= slots2[j][1]:
                j += 1
            elif duration <= min(slots1[i][1], slots2[j][1]) - max(slots1[i][0], slots2[j][0]):
                return [max(slots1[i][0], slots2[j][0]), max(slots1[i][0], slots2[j][0]) + duration]
            elif slots1[i][1] > slots2[j][1]:
                j += 1
            else:
                i += 1

        return []