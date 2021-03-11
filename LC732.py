class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1

        count = res = 0
        for i in sorted(self.delta):
            count += self.delta[i]
            if count > res:
                res = count

        return res